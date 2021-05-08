"""sahilportfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path
from backend.views import *
from django.conf.urls.static  import static
from backend.models import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('proj/<proj>/', proj_part),
    path('intern/<intern>/', intern_part),
    path('job/<job>/', job_part),
    path('cert/<cert>/',certif),
    path('all/', all_works),
    path('query_send', query_request,name="query"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_title = 'Gulfam Portfolio'
admin.site.site_header = 'Gulfam Portfolio'
admin.site.index_title = 'Gulfam Portfolio'