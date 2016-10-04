from django.conf.urls import url
from django.contrib import admin
from calculation import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url('^$', views.base),
    url(r'^admin/', admin.site.urls),
    url(r'^catalog/$', views.catalog),
    url('^search/$', views.search),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
