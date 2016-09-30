from django.conf.urls import url
from django.contrib import admin
from calculation import views

urlpatterns = [
    url('^$', views.base),
    url(r'^admin/', admin.site.urls),
    url(r'^catalog/$', views.catalog),
    url('^search/$', views.search),
]
