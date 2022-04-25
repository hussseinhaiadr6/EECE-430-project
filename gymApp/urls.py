"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path
#from django.conf.urls import url
from . import views

app_name="gymApp"
urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^signup$',views.signup, name='signup'),
    url(r'^login$',views.clientlogin, name='clientlogin'),
    url(r'^signout$',views.signout, name='signout'),
    url(r'^addClass$',views.createClass, name='createClass'),
    url(r'^viewschedule$',views.ClassSchedule, name='ClassSchedule'),
    url(r'^viewclasses$',views.viewclasses, name='viewclasses'),
    url(r'^db_delete_class/(?P<id>\d+)/$',views.db_delete_class,name='db_delete_class'),
    
    url(r'^viewinstructors$',views.viewinstructors, name='viewinstructors'),
    url(r'^manageclient$',views.manageclient, name='manageclient'),
    path('delete_client/<str:mail>/',views.delete_client,name='delete_client'),
    path('update_client/<str:mail>/',views.update_client,name='update_client'),
    path('membership/<str:type>/',views.membership,name='membership'),
    path('reserveclass/<str:id>/',views.reserveclass,name='reserveclass'),
    path('deletereservation/<str:id>/',views.deletereservation,name='deletereservation'),
    path('viewreservedclasses/',views.viewreservedclasses, name='viewreservedclasses'),
    url('admin/gymreport',views.gymreport, name='gymreport'),
    path('deletemembership/<str:id>/',views.deletemembership,name='deletemembership'),]


