import os
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        print(f"{os.environ=}")

        return context
