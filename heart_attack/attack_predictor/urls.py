from django.urls import path

from . import views

urlpatterns = [
    path('',views.home_page,name = 'home_page'),
    path('result',views.results_page,name = 'result_page')
]