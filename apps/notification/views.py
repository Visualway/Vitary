from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Notification
from django.core.paginator import Paginator



@login_required
def notification_page(request):
    notifications = Notification.objects.filter(to_user=request.user)
    paginator = Paginator(notifications, 10)
    page = request.GET.get('page')
    notifications = paginator.get_page(page)
    return render(request, 'notification/notification_page.html', {'notifications': notifications})


@login_required
def notification_redirect(request, pk):
    notification = Notification.objects.get(pk=pk)
    if notification.to_user == request.user:
        notification.is_read = True
        notification.save()
        return redirect(notification.link)
    else:
        return redirect('notification_page')

@login_required
def mark_all_as_read(request):
    user_notifications = Notification.objects.filter(to_user=request.user)
    for user_notification in user_notifications:
        user_notification.is_read = True
        user_notification.save()

    messages.success(request, 'All the notifications have been marked as read!')
    return redirect('notification_page')