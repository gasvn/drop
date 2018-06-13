from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('<int:NoteId>/', views.add, name='add'),
    #path('add/<int:NoteId>/<slug:NoteContent>', views.add, name='add'),
    #path('add/', views.add, name='read'),
   # path('read/<int:NoteId>', views.read, name='read'),
    # path('read/', views.read, name='read'), 
    path('submit/', views.submit, name='submit'),
    path('raw/<slug:NoteId>', views.raw, name='raw'),
    path('qrcode/',views.genqrcode,name='genqrcode'),
    path('rawlink/',views.genrawlink,name='genrawlink'),
]