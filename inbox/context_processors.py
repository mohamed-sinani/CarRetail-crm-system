def inquiry_count(request):
    if request.user.is_authenticated and request.user.is_staff:
        from .models import ChatSession,ChatMessage
        active_sessions=ChatSession.objects.filter(status=ChatSession.Status.ACTIVE)
        unread=ChatMessage.objects.filter(
            session__in=active_sessions,
            is_read=False,
        ).exclude(sender=request.user).count()
        return {"new_inquiry_count":unread}
    return {}
