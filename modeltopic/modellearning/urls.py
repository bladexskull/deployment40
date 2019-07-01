from django.urls import path
from modellearning import views

urlpatterns=[
    path('',views.formcall,name='formcall')
]
