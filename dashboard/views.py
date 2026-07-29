from datetime import timedelta
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count,Sum
from django.db.models.functions import TruncMonth
from django.shortcuts import get_object_or_404,redirect,render
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
    now=timezone.now()
    first_of_month=now.replace(day=1,hour=0,minute=0,second=0,microsecond=0)
    last_month_start=(first_of_month-timedelta(days=1)).replace(day=1)
    def pct(current,prev):
        if not prev:
            return "0%"
        change=((current-prev)/prev)*100
        sign="+"if change>=0 else ""
        return f"{sign}{change:.0f}%"
    prev_revenue=Sale.objects.filter(sale_date__lt=first_of_month).aggregate(total=Sum("amount"))["total"]or 0
    prev_deals=Deal.objects.filter(updated_at__lt=first_of_month).count()
    prev_vehicles=Vehicle.objects.filter(created_at__lt=first_of_month).count()if hasattr(Vehicle,"created_at")else 0
    prev_contacts=Customer.objects.filter(created_at__lt=first_of_month).count()if hasattr(Customer,"created_at")else 0
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
            {"title":"Sales / Revenue","value":f"{sales_count} / TZS {revenue:,.0f}","percent":pct(revenue,prev_revenue),"icon":"bi-cash-stack"},
            {"title":"Active Deals","value":active_deals,"percent":pct(active_deals,prev_deals),"icon":"bi-kanban"},
            {"title":"Total Vehicles","value":total_vehicles,"percent":pct(total_vehicles,prev_vehicles),"icon":"bi-car-front"},
            {"title":"Contacts","value":contacts_count,"percent":pct(contacts_count,prev_contacts),"icon":"bi-people"},
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
        return redirect("dashboard:home")
    if request.method=="POST":
        form=MarketingCampaignForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Marketing campaign saved.")
            return redirect("dashboard:marketing")
    else:
        form=MarketingCampaignForm()
    campaigns=[]
    for campaign in MarketingCampaign.objects.all():
        whatsapp_link=""
        if campaign.whatsapp_phone:
            phone="".join(char for char in campaign.whatsapp_phone if char.isdigit())
            if phone:
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
@login_required
def campaign_edit(request,pk):
    if request.user.role not in ("ADMIN","MARKETING") and not request.user.is_superuser:
        messages.error(request,"You do not have permission.")
        return redirect("dashboard:home")
    campaign=get_object_or_404(MarketingCampaign,pk=pk)
    if request.method=="POST":
        form=MarketingCampaignForm(request.POST,instance=campaign)
        if form.is_valid():
            form.save()
            messages.success(request,"Campaign updated.")
            return redirect("dashboard:marketing")
    else:
        form=MarketingCampaignForm(instance=campaign)
    return render(request,"form.html",{"form":form,"page_title":"Edit Campaign","object":campaign})
@login_required
def campaign_delete(request,pk):
    if request.user.role not in ("ADMIN","MARKETING") and not request.user.is_superuser:
        messages.error(request,"You do not have permission.")
        return redirect("dashboard:home")
    campaign=get_object_or_404(MarketingCampaign,pk=pk)
    if request.method=="POST":
        campaign.delete()
        messages.success(request,"Campaign deleted.")
        return redirect("dashboard:marketing")
    return render(request,"confirm_delete.html",{"object":campaign,"page_title":"Delete Campaign"})
