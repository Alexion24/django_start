from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.views import View


class Calc(TemplateView):

    template_name = 'calc/calc.html'

    def get_context_data(self, a, b, **kwargs):
        context = super().get_context_data(**kwargs)
        context['first_number'] = a
        context['second_number'] = b
        context['sum'] = (a + b)
        return context


class IndexView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('calc')
