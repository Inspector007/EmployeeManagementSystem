from django.conf.urls import url, include
from empapp import views

urlpatterns = [
    url(r'^$', views.employeeadd, name = 'employeeadd'),
    # url(r'^list$', views.employeelist, name = 'employeelist'),
    url(r'^list/$', views.EmployeeListView.as_view(), name = 'employeelist'),
    url(r'^detail/(?P<name>\w{1,20})/(?P<pan>\w{1,15})/$', 
    	views.employeedetail, name = 'employeedetail'),
]

