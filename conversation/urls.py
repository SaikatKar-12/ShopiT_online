from django.urls import path

from . import views
from .views import new_conversation, inbox, detail, delete_conversation
app_name = 'conversation'

urlpatterns = [
    path('',views.inbox,name='inbox'),
    path('<int:pk>/', views.detail, name='detail'),
    path('new/<int:item_pk>/',views.new_conversation, name = 'new_conversation'),
    path('delete/<int:pk>/', views.delete_conversation, name='delete_conversation'),
]