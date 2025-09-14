from django.urls import path
from . import views

urlpatterns = [
    path("", views.batch_list, name="batch_list"),
    path("batch/<int:batch_id>/", views.batch_detail, name="batch_detail"),
    path("batch/new/", views.batch_create, name="batch_create"),
    path("batch/<int:batch_id>/add-item/", views.contentitem_create, name="contentitem_create"),
]
