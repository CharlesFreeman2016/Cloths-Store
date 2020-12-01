from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='home'),
    path('<int:pk>/detail/', views.ProductDetailView.as_view(), name='detail'),
    path('result/', views.SearchResultView.as_view(), name='result'),
]