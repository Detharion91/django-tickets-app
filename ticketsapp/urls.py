from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from authentication.views import RegisterView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tickets/', include('tickets.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', RegisterView.as_view(), name='register'),
    path('', auth_views.LoginView.as_view(), name='login', kwargs={'redirect_authenticated_user': True}),
]
