from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("<str:name>",views.greet,name="greet"),
    path("shiv",views.shiv,name="shiv"),
    path("hi",views.hi,name="hi")
    
]