from django.shortcuts import render,get_object_or_404
from vehicles.models import Vehicle
from django.db.models import Q
from announcements.models import Announcement
from dashboard.models import MarketingCampaign
def home(request):
    query=request.GET.get('q','')
    vehicles=Vehicle.objects.filter(status=Vehicle.Status.AVAILABLE)
    if query:
        vehicles = vehicles.filter(
            Q(brand__icontains=query)|
            Q(model__icontains=query)
        )
    vehicle_count=vehicles.count()
    featured=vehicles[:6]
    remaining=vehicles[6:]
    brands=Vehicle.objects.filter(status=Vehicle.Status.AVAILABLE).values_list('brand',flat=True).distinct().order_by('brand')
    announcements=Announcement.objects.all()[:3]
    marketing_ads=MarketingCampaign.objects.all()[:3]
    return render(request, 'public/home.html', {
        'featured':featured,
        'remaining':remaining,
        'vehicle_count':vehicle_count,
        'brands':brands,
        'query':query,
        'announcements':announcements,
        'marketing_ads':marketing_ads,
    })
def vehicle_detail(request,pk):
    vehicle=get_object_or_404(Vehicle,pk=pk,status=Vehicle.Status.AVAILABLE)
    related_vehicles = Vehicle.objects.filter(
        status=Vehicle.Status.AVAILABLE,brand=vehicle.brand
    ).exclude(pk=vehicle.pk)[:4]
    return render(request, 'public/vehicle_detail.html', {
        'vehicle':vehicle,
        'related_vehicles':related_vehicles,
    })
