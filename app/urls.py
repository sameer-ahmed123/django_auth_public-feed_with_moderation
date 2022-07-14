from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="home"),
    path('reports', views.report, name="reports"),
    path("logout", views.logout, name="logout"),
    path('delete/<int:id>/', views.deletepost, name="delete"),
    path("report/<int:id>/", views.report_post, name="report_post"),
    path("hide_post/<int:id>/", views.Hide_post, name="hide_post"),
    path("Ban_user/<int:id>/",views.Ban_user, name="Ban_user"),

]