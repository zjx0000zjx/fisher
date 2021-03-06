"""fisher URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from rest_framework_bulk.routes import BulkRouter

import grids.views
import robots.views

router = BulkRouter()
router.register("grids", grids.views.GridViewSet, basename="grid")
router.register("robots", robots.views.RobotViewSet, basename="robot")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("allauth.account.urls")),
    path("robots/", include("robots.urls")),
    path("credentials/", include("credentials.urls")),
    path("api/", include(router.urls)),
]
