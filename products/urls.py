from django.urls import path
from products.views import ProductListView, ProductDetailView

app_name="products"
urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('detail/<slug:slug>/', ProductDetailView.as_view(), name='detail'),
]