fromdjango.contribimportmessages
fromdjango.contrib.auth.decoratorsimportlogin_required
fromdjango.db.modelsimportCount,Sum
fromdjango.httpimportHttpResponse
fromdjango.shortcutsimportredirect,render
fromsales.modelsimportSale
fromvehicles.modelsimportVehicle
@login_required
defreport_center(request):
    ifrequest.user.role!="ADMIN"andnotrequest.user.is_superuser:
        messages.error(request,"You do not have permission to access reports.")
        returnredirect("dashboard:home")
    revenue=Sale.objects.aggregate(total=Sum("amount"))["total"]or0
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
defexport_report(request,kind,fmt):
    ifrequest.user.role!="ADMIN"andnotrequest.user.is_superuser:
        messages.error(request,"You do not have permission to export reports.")
        returnredirect("dashboard:home")
    iffmt=="pdf":
        body=b"%PDF-1.4\n1 0 obj<<>>endobj\ntrailer<<>>\n%%EOF"
        response=HttpResponse(body,content_type="application/pdf")
        response["Content-Disposition"]=f'attachment; filename="{kind}-report.pdf"'
        returnresponse
    rows=["Vehicle,Customer,Amount,Date"]
    forsaleinSale.objects.select_related("vehicle","customer"):
        rows.append(f'"{sale.vehicle}","{sale.customer}",{sale.amount},{sale.sale_date}')
    response=HttpResponse("\n".join(rows),content_type="application/vnd.ms-excel")
    response["Content-Disposition"]=f'attachment; filename="{kind}-report.xls"'
    returnresponse
