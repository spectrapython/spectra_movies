from . import views
from django.urls import path, include
app_name='movieapp'
urlpatterns = [
    path('',views.index,name='index'),
    path('movie/<int:movie_id>/',views.detail,name='detail'),
    path('add/',views.addmovie,name='addmovie'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('addi/<int:id>/',views.addi,name='addi')
 ]