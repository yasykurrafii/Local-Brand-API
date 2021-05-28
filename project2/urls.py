from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
    path("", views.apiOverview , name='article'),
    path('brand/', views.BrandList, name='brand'),
    path('brand/<int:pk>', views.DetailBrand, name='detailBrand'),
    path('product/', views.ProductList, name='product'),
    path('product/<str:tp>/', views.ProductType, name='product_type'),
    path('product/<int:pk>', views.DetailProduct, name='detailProduct'),
    path('api-token-auth/', obtain_auth_token),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('brand/<str:pk>', views.UpdateBrand, name='updatebrand'),
    # path('cloth/', views.ClothList, name='cloth'),
    # path('task-list/<str:pk>/', views.TaskDetail, name = 'daetail'),
    # path('task-create/', views.TaskCreate, name='create'),
    # path('task-update/<str:pk>/', views.TaskUpdate, name='update'),
    # path('task-delete/<str:pk>/', views.TaskDelete, name='delete')
]