from django.urls import path
from maths import views
urlpatterns=[
    path("",views.home,name="home"),
    path('add',views.add_num,name="addition"),
    path('sub',views.sub_num,name="subtraction"),
    path('mul',views.mul_num,name="multiplication"),
    path('div',views.div_num,name="division"),
    path('cube',views.cube_num,name="cube")
]