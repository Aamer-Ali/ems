from django.urls import path
from poll.views import index,details

urlpatterns = [
    path('',index, name='polls_list'),
    path('details/<int:id>',details, name='poll_details')
]
