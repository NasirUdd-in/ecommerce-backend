from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from .views import ProductList,  CustomTokenObtainPairView

urlpatterns = [
    path('products/', ProductList.as_view(), name='product-list'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)