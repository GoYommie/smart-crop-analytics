from django.urls import path
from . import views

urlpatterns = [
    # Home page (data table)
    path('', views.home, name='home'),

    # Charts page
    path('charts/', views.chart_page, name='chart_page'),
]