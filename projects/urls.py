from django.urls import path

from projects.views import HomePageView


app_name = "projects"
urlpatterns = [
    path("", HomePageView.as_view(), name="homepage"),
]
