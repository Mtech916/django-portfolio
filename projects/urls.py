from django.urls import path

from projects.views import HomePageView, ProjectDetailView


app_name = "projects"
urlpatterns = [
    path("project/<int:pk>", ProjectDetailView.as_view(), name="project-details"),
    path("", HomePageView.as_view(), name="homepage"),
]
