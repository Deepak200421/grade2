from django.contrib import admin
from django.urls import path, include
from grades import views as grades_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('grades.urls')),
    path('register/', grades_views.register, name='register'),
    path('profile/', grades_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='grades/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='grades/logout.html'), name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
