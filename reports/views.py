from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Count,Sum
from django.http import HttpResponse
from django.shortcuts import redirect,render
from sales.models import Sale
from vehicles.models import Vehicle
@login_required
def report_center(request):
    if request.user.role!="ADMIN"and notrequest.user.is_superuser:
        messages.error(request,"You do not have permission to access reports.")
        returnredirect("dashboard:home")
    revenue=Sale.objects.aggregate(total=Sum("amount"))["total"]or 0
    context = {
        "page_title":"Reports",
        "sales_count":Sale.objects.count(),
        "revenue":revenue,
        "inventory_count":Vehicle.objects.count(),
        "available_count":Vehicle.objects.filter(status=Vehicle.Status.AVAILABLE).count(),
        "status_rows":Vehicle.objects.values("status").annotate(total=Count("id")),
        "top_sales":Sale.objects.select_related("vehicle","customer","salesperson")[:8],
    }
    returnrender(request,"reports.html",context)
@login_required
def export_report(request,kind,fmt):
    if request.user.role!="ADMIN"and notrequest.user.is_superuser:
        messages.error(request,"You do not have permission to export reports.")
        returnredirect("dashboard:home")
    if fmt=="pdf":
        body=b"%PDF-1.4\n1 0 obj<<>>endobj\ntrailer<<>>\n%%EOF"
        response=HttpResponse(body,content_type="application/pdf")
        response["Content-Disposition"]=f'attachment; filename="{kind}-report.pdf"'
        returnresponse
    rows=["Vehicle,Customer,Amount,Date"]
    for sale in Sale.objects.select_related("vehicle","customer"):
        rows.append(f'"{sale.vehicle}","{sale.customer}",{sale.amount},{sale.sale_date}')
    response=HttpResponse("\n".join(rows),content_type="application/vnd.ms-excel")
    response["Content-Disposition"]=f'attachment; filename="{kind}-report.xls"'
    returnresponse
