"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path , include
from django.conf.urls.static import static
from . import settings
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),                 #로그인은 장고에서 제공 form/view에서 안만들어도됨
    path('accounts/register/', views.UserCreateView.as_view(), name='register'),
    path('accounts/register/done/', views.UserCreateDoneTV.as_view(), name='register_done'),
    path('',views.HomeView.as_view(), name='index'), #첫페이지
    

    # path('news/',views.NewsView.as_view(),name='news'),  #뉴스페이지
    path('movie/', include('movie.urls')),
    
    path('blog/',include('blog.urls')),
    # path("cafe/", include("cafe.urls")),
    path("imageapp/", include("imageapp.urls")),
    
    ]



if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
        
    ] + urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #이미지

