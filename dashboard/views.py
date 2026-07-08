from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count,Sum
from django.db.models.functions import TruncMonth
from django.shortcuts import redirect,render
from django.utils import timezone
from urllib.parse import quote
from announcements.models import Announcement
from customers.models import Customer
from deals.models import Deal
from .forms import MarketingCampaignForm
from .models import MarketingCampaign
from sales.models import Sale
from vehicles.models import Vehicle
@login_required
def dashboard_home(request):
    user=request.user
    if user.role=="SALES":
        sales_count=Sale.objects.filter(salesperson=user).count()
        revenue=Sale.objects.filter(salesperson=user).aggregate(total=Sum("amount"))["total"] or 0
        active_deals=Deal.objects.filter(salesperson=user).exclude(stage__in=[Deal.Stage.CLOSED_WON,Deal.Stage.CLOSED_LOST]).count()
        contacts_count=Customer.objects.filter(assigned_salesperson=user).count()
        total_vehicles=Vehicle.objects.count()
        monthly_sales = (
            Sale.objects.filter(salesperson=user)
            .annotate(month=TruncMonth("sale_date"))
            .values("month")
            .annotate(total=Sum("amount"))
            .order_by("month")
        )
        recent_sales=Sale.objects.filter(salesperson=user).select_related("vehicle","customer")[:5]
        recent_deals=Deal.objects.filter(salesperson=user).select_related("vehicle","customer")[:5]
        announcements=Announcement.objects.all()[:5]
        status_counts=Vehicle.objects.values("status").annotate(total=Count("id"))
    elif user.role=="MARKETING":
        sales_count=Sale.objects.count()
        revenue=Sale.objects.aggregate(total=Sum("amount"))["total"] or 0
        active_deals=Deal.objects.count()
        contacts_count=Customer.objects.count()
        total_vehicles=Vehicle.objects.count()
        monthly_sales = (
            Sale.objects.annotate(month=TruncMonth("sale_date"))
            .values("month")
            .annotate(total=Sum("amount"))
            .order_by("month")
        )
        recent_sales=Sale.objects.select_related("vehicle","customer","salesperson")[:5]
        recent_deals=[]
        announcements=Announcement.objects.select_related("created_by")[:5]
        status_counts=Vehicle.objects.values("status").annotate(total=Count("id"))
    else:
        total_vehicles=Vehicle.objects.count()
        sales_count=Sale.objects.count()
        revenue=Sale.objects.aggregate(total=Sum("amount"))["total"] or 0
        active_deals=Deal.objects.exclude(stage__in=[Deal.Stage.CLOSED_WON,Deal.Stage.CLOSED_LOST]).count()
        contacts_count=Customer.objects.count()
        monthly_sales = (
            Sale.objects.annotate(month=TruncMonth("sale_date"))
            .values("month")
            .annotate(total=Sum("amount"))
            .order_by("month")
        )
        recent_sales=Sale.objects.select_related("vehicle","customer","salesperson")[:5]
        recent_deals=Deal.objects.select_related("vehicle","customer","salesperson")[:5]
        announcements=Announcement.objects.select_related("created_by")[:5]
        status_counts=Vehicle.objects.values("status").annotate(total=Count("id"))
    sales_labels=[item["month"].strftime("%b") for item in monthly_sales if item["month"]]
    sales_values=[float(item["total"] or 0) for item in monthly_sales]
    if not sales_labels:
        sales_labels=["Jan","Feb","Mar","Apr","May","Jun"]
        sales_values=[18000,22000,19500,28000,31000,36000]
    status_map={item["status"]:item["total"]for item in status_counts}
    activities = [
        {"title":f"Sold {sale.vehicle}","meta":f"{sale.customer} - {sale.sale_date:%d %b %Y}"}
        for sale in recent_sales
    ]
    activities += [
        {"title":f"{deal.get_stage_display()} deal","meta":f"{deal.customer} - {deal.vehicle}"}
        for deal in recent_deals
    ]
    context = {
        "page_title":"Dashboard",
        "stats": [
            {"title":"Sales / Revenue","value":f"{sales_count} / TZS {revenue:,.0f}","percent":"+18%","icon":"bi-cash-stack"},
            {"title":"Active Deals","value":active_deals,"percent":"+5%","icon":"bi-kanban"},
            {"title":"Total Vehicles","value":total_vehicles,"percent":"+12%","icon":"bi-car-front"},
            {"title":"Contacts","value":contacts_count,"percent":"+8%","icon":"bi-people"},
        ],
        "sales_labels":sales_labels,
        "sales_values":sales_values,
        "vehicle_status_values": [
            status_map.get(Vehicle.Status.AVAILABLE,0),
            status_map.get(Vehicle.Status.RESERVED,0),
            status_map.get(Vehicle.Status.SOLD,0),
        ],
        "activities":activities[:6],
        "announcements":announcements,
        "today":timezone.localdate(),
    }
    return render(request,"dashboard.html",context)
@login_required
def marketing_home(request):
    if request.user.role not in ("ADMIN","MARKETING") and not request.user.is_superuser:
        messages.error(request,"You do not have permission to access marketing.")
        returnredirect("dashboard:home")
    if request.method=="POST":
        form=MarketingCampaignForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Marketing campaign saved.")
            returnredirect("dashboard:marketing")
    else:
        form=MarketingCampaignForm()
    campaigns=[]
    for campaign in MarketingCampaign.objects.all():
        whatsapp_link=""
        if campaign.whatsapp_phone:
            phone="".join(char for char in campaign.whatsapp_phone if char.isdigit())
            whatsapp_link=f"https://wa.me/{phone}?text={quote(campaign.message)}"
        campaigns.append({"campaign":campaign,"whatsapp_link":whatsapp_link})
    context = {
        "page_title":"Marketing",
        "form":form,
        "campaigns":campaigns,
        "channel_count":len(MarketingCampaign.Channel.choices),
        "total_views":sum(item["campaign"].views for item in campaigns),
        "total_replies":sum(item["campaign"].replies for item in campaigns),
        "total_leads":sum(item["campaign"].leads for item in campaigns),
        "announcements":Announcement.objects.all()[:3],
    }
    return render(request,"marketing.html",context)
