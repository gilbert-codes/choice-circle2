from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("choose/<int:participant_id>/", views.choose, name="choose"),
    path("result/<int:participant_id>/", views.result, name="result"),
    path("admin-dashboard/", views.admin_dashboard, name="admin_dashboard"),
    path("reset/<int:participant_id>/", views.reset_participant_choice, name="reset_participant_choice"),
]
