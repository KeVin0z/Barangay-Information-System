from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('create_residents', views.create_residents, name='create_residents'),
    path('create_residents/create', views.process_create_resident, name='process_create_resident'),
    path('list_residents', views.list_residents, name='list_residents'),
    path('edit_resident/<pk>', views.edit_resident, name='edit_resident'),
    path('edit_residents/edit/<pk>', views.process_edit_resident, name='process_edit_resident'),
    path('delete_resident/<pk>', views.process_delete_resident, name='process_delete_resident'),
    path('create_officials', views.create_officials, name='create_officials'),
    path('create_officials/create', views.process_create_official, name='process_create_official'),
    path('list_officials', views.list_officials, name='list_officials'),
    path('edit_official/<pk>', views.edit_official, name='edit_official'),
    path('edit_officials/edit/<pk>', views.process_edit_official, name='process_edit_official'),
    path('create_blotters', views.create_blotters, name='create_blotters'),
    path('create_blotters/create', views.process_create_blotter, name='process_create_blotter'),
    path('list_blotters', views.list_blotters, name='list_blotters'),
    path('edit_blotter/<pk>', views.edit_blotter, name='edit_blotter'),
    path('edit_blotters/edit/<pk>', views.process_edit_blotter, name='process_edit_blotter'),
    path('delete_blotter/<pk>', views.process_delete_blotter, name='process_delete_blotter'),
    path('create_sks', views.create_sks, name='create_sks'),
    path('create_sks/create', views.process_create_sk, name='process_create_sk'),
    path('list_sks', views.list_sks, name='list_sks'),
    path('edit_sk/<pk>', views.edit_sk, name='edit_sk'),
    path('edit_sks/edit/<pk>', views.process_edit_sk, name='process_edit_sk'),

]