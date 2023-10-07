from django.views.generic import DetailView, TemplateView
from projects.models import Project
from django.urls import reverse


class HomePageView(TemplateView):
    template_name = "projects/all_projects.html"

    def get_context_data(self, **kwargs):
        # Query the db to return all project objecst
        context = super().get_context_data(**kwargs)
        context["projects"] = Project.objects.all()
        return context


class ProjectDetailView(DetailView):
    model = Project
    template_name = "projects/project_detail.html"

    def get_absolute_url(self):
        return reverse("project-details")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pk"] = self.object.pk
        return context
