from django.views.generic.base import TemplateView
from django.shortcuts import redirect
from django.urls import reverse


def my_view(request):
    return redirect(reverse('calc', kwargs={'a': 40, 'b': 2}))


class IndexPageView(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['who'] = 'World'
        return context
