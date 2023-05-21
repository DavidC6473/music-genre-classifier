from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from classifier import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', views.upload_file),
    path('result/<int:music_file_id>/', views.get_classification_result),
    path('', TemplateView.as_view(template_name='index.html')),
]
