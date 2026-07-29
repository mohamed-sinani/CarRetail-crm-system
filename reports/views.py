from io import BytesIO
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Count,Sum
from django.db.models.functions import TruncMonth
from django.http import HttpResponse
from django.shortcuts import redirect,render
from openpyxl import Workbook
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from sales.models import Sale
from vehicles.models import Vehicle
@login_required
def report_center(request):
    if request.user.role!="ADMIN" and not request.user.is_superuser:
        messages.error(request,"You do not have permission to access reports.")
        return redirect("dashboard:home")
    revenue=Sale.objects.aggregate(total=Sum("amount"))["total"]or 0
    context = {
        "page_title":"Reports",
        "sales_count":Sale.objects.count(),
        "revenue":revenue,
        "inventory_count":Vehicle.objects.count(),
        "available_count":Vehicle.objects.filter(status=Vehicle.Status.AVAILABLE).count(),

        "top_sales":Sale.objects.select_related("vehicle","customer","salesperson")[:8],
    }
    return render(request,"reports.html",context)
@login_required
def export_report(request,kind,fmt):
    if request.user.role!="ADMIN" and not request.user.is_superuser:
        messages.error(request,"You do not have permission to export reports.")
        return redirect("dashboard:home")
    qs=Sale.objects.select_related("vehicle","customer","salesperson")
    if kind=="inventory":
        qs=Vehicle.objects.all()
    if fmt=="pdf":
        buf=BytesIO()
        p=canvas.Canvas(buf,pagesize=A4)
        width,height=A4
        p.setFont("Helvetica-Bold",16)
        p.drawString(inch,height-inch,f"{kind.title()} Report")
        p.setFont("Helvetica",10)
        y=height-1.5*inch
        if kind=="sales":
            for sale in qs:
                p.drawString(inch,y,f"{sale.vehicle} - {sale.customer} - TZS {sale.amount:,.0f} - {sale.sale_date}")
                y-=14
                if y<inch:
                    p.showPage()
                    y=height-inch
        elif kind=="revenue":
            monthly=Sale.objects.annotate(month=TruncMonth("sale_date")).values("month").annotate(total=Sum("amount")).order_by("month")
            total=Sale.objects.aggregate(total=Sum("amount"))["total"]or 0
            for item in monthly:
                p.drawString(inch,y,f"{item['month'].strftime('%b %Y')} - TZS {item['total']:,.0f}")
                y-=14
            p.drawString(inch,y-14,f"Total Revenue - TZS {total:,.0f}")
        else:
            for v in qs:
                p.drawString(inch,y,f"{v.brand} {v.model} ({v.year}) - {v.status} - TZS {v.price:,.0f}")
                y-=14
                if y<inch:
                    p.showPage()
                    y=height-inch
        p.save()
        buf.seek(0)
        response=HttpResponse(buf.read(),content_type="application/pdf")
        response["Content-Disposition"]=f'attachment; filename="{kind}-report.pdf"'
        return response
    wb=Workbook()
    ws=wb.active
    ws.title=kind.title()
    if kind=="sales":
        ws.append(["Vehicle","Customer","Salesperson","Amount","Date"])
        for sale in qs:
            ws.append([str(sale.vehicle),str(sale.customer),str(sale.salesperson),sale.amount,str(sale.sale_date)])
    elif kind=="revenue":
        ws.append(["Month","Total"])
        monthly=Sale.objects.annotate(month=TruncMonth("sale_date")).values("month").annotate(total=Sum("amount")).order_by("month")
        for item in monthly:
            ws.append([item["month"].strftime("%b %Y"),item["total"]])
        ws.append(["Total Revenue",Sale.objects.aggregate(total=Sum("amount"))["total"]or 0])
    else:
        ws.append(["Brand","Model","Year","Price","Mileage","Transmission","Fuel","Status"])
        for v in qs:
            ws.append([v.brand,v.model,v.year,v.price,v.mileage,v.get_transmission_display(),v.get_fuel_type_display(),v.get_status_display()])
    buf=BytesIO()
    wb.save(buf)
    buf.seek(0)
    response=HttpResponse(buf.read(),content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response["Content-Disposition"]=f'attachment; filename="{kind}-report.xlsx"'
    return response
