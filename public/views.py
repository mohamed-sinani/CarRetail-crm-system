from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404
from django.db import IntegrityError
from vehicles.models import Vehicle
from django.db.models import Q
from announcements.models import Announcement
from dashboard.models import MarketingCampaign
from accounts.models import User
from inbox.models import ChatSession

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
    announcements=Announcement.objects.all()[:3]
    marketing_ads=MarketingCampaign.objects.all()[:3]
    return render(request, 'public/home.html', {
        'featured':featured,
        'remaining':remaining,
        'vehicle_count':vehicle_count,
        'query':query,
        'announcements':announcements,
        'marketing_ads':marketing_ads,
        'dealer_phone':getattr(settings,'DEALER_PHONE','+254700000000'),
    })

def vehicle_detail(request,pk):
    vehicle=get_object_or_404(Vehicle,pk=pk,status=Vehicle.Status.AVAILABLE)
    related_vehicles = Vehicle.objects.filter(
        status=Vehicle.Status.AVAILABLE,brand=vehicle.brand
    ).exclude(pk=vehicle.pk)[:4]
    return render(request, 'public/vehicle_detail.html', {
        'vehicle':vehicle,
        'related_vehicles':related_vehicles,
        'dealer_phone':getattr(settings,'DEALER_PHONE','+254700000000'),
    })

def register(request):
    if request.user.is_authenticated:
        return redirect("public_home")
    if request.method=="POST":
        username=request.POST.get("username","").strip()
        email=request.POST.get("email","").strip()
        phone=request.POST.get("phone","").strip()
        password=request.POST.get("password","")
        if not username or not email or not password:
            messages.error(request,"All fields are required.")
            return render(request,"public/register.html")
        if User.objects.filter(username=username).exists():
            messages.error(request,"Username already taken.")
            return render(request,"public/register.html")
        if User.objects.filter(email=email).exists():
            messages.error(request,"Email already registered.")
            return render(request,"public/register.html")
        user=User.objects.create_user(username=username,email=email,password=password,role=User.Role.CUSTOMER)
        user.phone=phone
        user.save(update_fields=["phone"])
        login(request,user)
        messages.success(request,"Account created! You can now chat with us.")
        next_url=request.GET.get("next","public_home")
        return redirect(next_url)
    return render(request,"public/register.html")

def customer_login(request):
    if request.user.is_authenticated:
        return redirect("public_home")
    if request.method=="POST":
        username=request.POST.get("username","").strip()
        password=request.POST.get("password","")
        user=authenticate(request,username=username,password=password)
        if user is not None and user.role==User.Role.CUSTOMER:
            login(request,user)
            next_url=request.GET.get("next","public_home")
            return redirect(next_url)
        messages.error(request,"Invalid username or password.")
    return render(request,"public/login.html")

def customer_logout(request):
    logout(request)
    return redirect("public_home")

@login_required
def chat_room(request,pk):
    vehicle=get_object_or_404(Vehicle,pk=pk,status=Vehicle.Status.AVAILABLE)
    session,created=ChatSession.objects.get_or_create(
        vehicle=vehicle,customer=request.user,
        defaults={"status":ChatSession.Status.ACTIVE},
    )
    return render(request,"public/chat.html",{
        "session":session,
        "vehicle":vehicle,
    })
