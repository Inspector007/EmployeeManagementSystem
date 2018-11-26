from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from restapi import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'users', views.GroupViewSet)


urlpatterns = [
    # url(r'^', include(router.urls)),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'all_emp/$', views.employeeList.as_view()),
    url(r'emp/(?P<pk>[0-9]+)/$',views.employeeDetail.as_view()),	
]


urlpatterns = format_suffix_patterns(urlpatterns)
