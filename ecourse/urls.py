"""
URL configuration for ecourse project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from authen.views import RegisterView

urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path("course/", include("course_manager.urls"), name="course"),
    path("student/", include("student.urls"), name="student"),
    path("study/", include("study.urls"), name="study"),
    path(r"^webpush/", include("webpush.urls")),
    path("accounts/social/signup/", RegisterView.as_view(), name="account_signup"),
    path("accounts/", include("allauth.urls")),
    path("", include("authen.urls")),
]

if settings.DEBUG == True:
    urlpatterns.append(path("__debug__/", include("debug_toolbar.urls")))

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
