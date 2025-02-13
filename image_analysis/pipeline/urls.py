from django.urls import path
from . import views
urlpatterns = [
    path('image-analysis/', views.ImageAnalysisView.as_view(), name='image-analysis-view')
]