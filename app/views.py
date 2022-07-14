from django.shortcuts import render,redirect
from django.contrib.auth import  get_user_model,logout as django_logout
from django.contrib.auth.decorators import login_required, permission_required
from django.conf import settings
from app.forms import postForm
from app.models import post, Report ,User
from django.db.models import Count
from datetime import datetime

# Create your views here.

def index(request):
    if request.method == "POST":
        form = postForm(request.POST)
        if form.is_valid():
            post1 = form.save(commit=False)
            post1.user = request.user
            post1.save()
            return redirect("/")
    else:
        form =postForm()
        posts = post.objects.filter(hidden=False).order_by("-date_posted").all()
    return render(request, "home.html", {"form": form, "posts": posts})

def deletepost(request, id):
    Posts = post.objects.get(id=id)
    if post.user == request.user:
        Posts.delete()
    return redirect("/")


@permission_required("app.view_report", raise_exception=True)
def report(request):
    reports = post.objects.annotate(times_reported=Count('report')).filter(times_reported__gt=0).all()
    return render(request, "reports.html",{"reports": reports})

@permission_required("app.view_report",raise_exception=True)
def Hide_post(request, id):
    hide =post.objects.get(id=id)
    hide.hidden= True
    hide.date_hidden =datetime.now()
    hide.hidden_by =request.user
    hide.save()
    return redirect("/reports")

@permission_required("app.change_user", raise_exception=True)
def Ban_user(request, id):
    users = get_user_model()
    user =User.objects.get(id=id)
    for post in user.post_set.all():
        if not post.hidden :
            post.hidden = True
            post.date_hidden =datetime.now()
            post.hidden_by = request.user
            post.save()

    user.is_active = False
    user.save()
    return redirect("/reports")
def report_post(request, id):
    post1 = post.objects.get(id=id)
    report, created = Report.objects.get_or_create(reported_by=request.user, post_reported=post1)

    if created:
        report.save()

    return redirect("/")


@login_required
def logout(request):
    django_logout(request)
    domain = settings.SOCIAL_AUTH_AUTH0_DOMAIN
    client_id = settings.SOCIAL_AUTH_AUTH0_KEY
    return_to = "http://127.0.0.1:8000"
    return redirect(f"https://{domain}/v2/logout?client_id={client_id}&returnTo={return_to}")
