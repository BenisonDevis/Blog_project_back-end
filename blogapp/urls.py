from django.urls import path
from .views import *

urlpatterns = [
   path('blog/create',BlogCreateApiView.as_view())
]
