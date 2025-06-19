from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView
from myapp import views  # Предполагается, что представления находятся в приложении myapp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('data/', views.data_view, name='data'),
    path('test/', views.test_view, name='test'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]