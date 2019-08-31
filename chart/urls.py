from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from chart import views

urlpatterns = [
    path('chart/', views.ChartList.as_view()),
    path('chart/<int:pk>/', views.ChartDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)