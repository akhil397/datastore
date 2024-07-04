from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_btn, name='search_btn'),
    path('add/', views.adddata, name='adddata'),
    path('about/<int:pk>/', views.about, name='about'),
    path('update/<int:pk>/', views.update_code_model, name='update_data'),
    path('delete/<int:pk>/', views.delete_data, name='delete_data'),
    # path('details/<int:pk>/', views.details, name='details'),
]
