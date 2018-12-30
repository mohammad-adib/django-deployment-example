from django.urls import path
from app_one import views

# TEMPLATE TAGGING
app_name='app_one'

urlpatterns=[
    path('other/',views.other,name='other'),
    path('relative/',views.relative,name='relative'),
]
