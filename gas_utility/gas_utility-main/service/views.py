# service/views.py
from django.shortcuts import render, redirect
from .models import ServiceRequest, Notification, Comment
from .forms import ServiceRequestForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

@login_required
def create_service_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.user = request.user
            service_request.save()
            return redirect('request_status', service_request.id)
    else:
        form = ServiceRequestForm()
    return render(request, 'service/create_request.html', {'form': form})

@login_required
def request_status(request, request_id):
    service_request = ServiceRequest.objects.get(id=request_id)
    comments = service_request.comments.all()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.request = service_request
            comment.save()
    else:
        comment_form = CommentForm()

    return render(request, 'service/request_status.html', {
        'service_request': service_request,
        'comments': comments,
        'comment_form': comment_form
    })

@login_required
def notifications(request):
    notifications = Notification.objects.filter(user=request.user, is_read=False)
    return render(request, 'service/notifications.html', {'notifications': notifications})

@staff_member_required
def admin_dashboard(request):
    requests = ServiceRequest.objects.all().order_by('-created_at')
    return render(request, 'service/admin_dashboard.html', {'requests': requests})
