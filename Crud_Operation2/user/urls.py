from django.urls import path


from .views import *

urlpatterns = [
    path('', listview, name='List'),
    path('create/', createview, name='create'),
    path('edit/<int:pk>/', editview, name='edit'),
    path('delete/<int:pk>/', deleteview, name='delete'),
]