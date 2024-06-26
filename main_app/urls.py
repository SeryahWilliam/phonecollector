from django.urls import path
from . import views
	
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('phones/', views.phones_index, name='index'),
    path('phones/<int:phone_id>', views.phones_detail, name='detail'),
    path('phones/create/', views.PhoneCreate.as_view(), name='phones_create'),
    path('phones/<int:pk>/update/', views.PhoneUpdate.as_view(), name='phones_update'),
    path('phones/<int:pk>/delete/', views.PhoneDelete.as_view(), name='phones_delete'),
    path('phones/<int:phone_id>/add_repair/', views.add_repair, name='add_repair'),
    path('accessory/', views.AccessoryList.as_view(), name='accessories_index'),
    path('accessory/<int:pk>/', views.AccessoryDetail.as_view(), name='accessories_detail'),
    path('accessory/create/', views.AccessoryCreate.as_view(), name='accessories_create'),
    path('accessory/<int:pk>/update/', views.AccessoryUpdate.as_view(), name='accessory_update'),
    path('accessory/<int:pk>/delete/', views.AccessoryDelete.as_view(), name='accessory_delete'),
    path('phones/<int:phone_id>/assoc_accessory/<int:accessory_id>/', views.assoc_accessory, name='assoc_accessory'),
    path('phones/<int:phone_id>/remove_accessory/<int:accessory_id>/', views.remove_accessory, name='remove_accessory'),
    path('phones/<int:phone_id>/add_photo/', views.add_photo, name='add_photo'),
    path('accounts/signup/', views.signup, name='signup'),
    
]


