"""Definiuje wzorce adresów URL dla learning_logs."""

from django.urls import  path

from  . import  views

app_name = 'learning_logs'
urlpatterns = [
    #Strona głowna.
    path('', views.index, name='index'),
    path('topics', views.topics, name='topics'),
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    #Strona przeznaczona do dodawania nowego tematu.
    path('new_topic/', views.new_topic, name='new_topic'),
    #Strona przeznaczona do dodawania nowego wpisu.
    path('new_entry/<int:topic_id>', views.new_entry, name ='new_entry'),
    #Stron przeznaczona do edycji wpisu
    path('edit_entry/<int:entry_id>', views.edit_entry, name='edit_entry'),
]