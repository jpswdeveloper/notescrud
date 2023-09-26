from django.urls import path
from api import views

urlpatterns=[
    path('',views.note_list_view),
    path('<int:pk>/',views.note_update_delete)
]