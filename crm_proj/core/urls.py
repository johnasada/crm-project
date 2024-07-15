from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("create-record/", views.create_record, name="create-record"),
    path("record-detail/<int:pk>/", views.record_detail, name="record-detail"),
    path("update-record/<int:pk>/", views.update_record, name="update-record"),
    path("delete-record/<int:pk>/", views.delete_record, name="delete-record"),
]
