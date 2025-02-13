from django.urls import path
from . import views
urlpatterns = [
    path('image_analysis/', views.ImageAnalysisView.as_view(), name='image-analysis-view')
]