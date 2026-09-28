from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),

    path(
        'notes/',
        views.notes_list,
        name='notes'
    ),

    path(
        'upload/',
        views.upload_note,
        name='upload'
    ),

    path(
        'about/',
        views.about,
        name='about'
    ),

    path(
        'contact/',
        views.contact,
        name='contact'
    ),

    path(
        'admin-login/',
        views.admin_login,
        name='admin_login'
    ),

    path(
        'dashboard/',
        views.dashboard,
        name='dashboard'
    ),

    path(
        'admin-logout/',
        views.admin_logout,
        name='admin_logout'
    ),
]
