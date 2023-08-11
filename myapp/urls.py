from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('product', views.product),
    path('hello/<str:username>', views.hello),
    path('number/<int:num>', views.number),
    path('projects/<str:p_name>', views.projects),
    path('tasks/<int:id>', views.tasks),
    
    
]