
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include('shebaApp.urls')),
    
    # path('register/',user_views.register, name='register'),
    # path('login/',user_views.LoginView.as_view(template_name='login.html'), name='login'),
    # path('logout/',user_views.LogoutView.as_view(template_name='logout.html'), name='logt'),
]
