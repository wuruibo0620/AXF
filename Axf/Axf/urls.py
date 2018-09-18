
from django.conf.urls import url, include
from django.contrib import admin
from axf_app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/$', views.index, name='index'),
    url(r'^axf/',include("axf_app.urls",namespace='axf'))
]
