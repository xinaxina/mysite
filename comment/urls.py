from django.urls import path
from . import views

# http://localhost:8000/blog/1

urlpatterns = [
    path('update_comment', views.update_conment, name='update_comment')
]
