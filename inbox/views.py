from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404,redirect,render
from django.views.decorators.http import require_POST
from .forms import ChatMessageForm
from .models import ChatSession,ChatMessage

@login_required
def chat_list(request):
    qs=ChatSession.objects.filter(customer__role="CUSTOMER").select_related("vehicle","customer","assigned_to").prefetch_related("messages")
    tab=request.GET.get("tab","active")
    if tab=="active":
        qs=qs.filter(status=ChatSession.Status.ACTIVE)
    elif tab=="closed":
        qs=qs.filter(status=ChatSession.Status.CLOSED)
    return render(request,"inbox/list.html",{
        "page_title":"Chats",
        "sessions":qs,
        "tab":tab,
    })

@login_required
def chat_detail(request,pk):
    session=get_object_or_404(ChatSession,pk=pk)
    if request.method=="POST":
        if request.POST.get("close"):
            session.status=ChatSession.Status.CLOSED
            session.save(update_fields=["status"])
            messages.success(request,"Chat closed.")
            return redirect("inbox:list")
        form=ChatMessageForm(request.POST)
        if form.is_valid():
            msg=form.save(commit=False)
            msg.session=session
            msg.sender=request.user
            msg.save()
            session.assigned_to=request.user
            session.save(update_fields=["assigned_to"])
            return redirect("inbox:detail",pk=pk)
    else:
        form=ChatMessageForm()
    ChatMessage.objects.filter(session=session,is_read=False).exclude(sender=request.user).update(is_read=True)
    return render(request,"inbox/detail.html",{
        "page_title":f"Chat: {session.customer.username}",
        "session":session,
        "form":form,
    })

@login_required
@require_POST
def send_message_api(request):
    import json
    data=json.loads(request.body)
    session=get_object_or_404(ChatSession,pk=data["session_id"])
    if request.user!=session.customer and request.user.role not in("ADMIN","SALES","MARKETING"):
        return JsonResponse({"error":"Forbidden"},status=403)
    msg=ChatMessage.objects.create(
        session=session,
        sender=request.user,
        message=data["message"],
    )
    if request.user.role!="CUSTOMER":
        session.assigned_to=request.user
        session.save(update_fields=["assigned_to"])
    return JsonResponse({
        "id":msg.pk,
        "sender":request.user.username,
        "message":msg.message,
        "created_at":msg.created_at.isoformat(),
    })

@login_required
def fetch_messages_api(request):
    session_id=request.GET.get("session_id")
    after_id=request.GET.get("after",0)
    session=get_object_or_404(ChatSession,pk=session_id)
    if request.user!=session.customer and request.user.role not in("ADMIN","SALES","MARKETING"):
        return JsonResponse({"error":"Forbidden"},status=403)
    qs=ChatMessage.objects.filter(session=session,pk__gt=after_id)
    if not request.user.is_staff:
        qs.filter(is_read=False).exclude(sender=request.user).update(is_read=True)
    return JsonResponse({
        "messages":[
            {
                "id":m.pk,
                "sender":m.sender.username,
                "message":m.message,
                "created_at":m.created_at.isoformat(),
            }
            for m in qs
        ]
    })
