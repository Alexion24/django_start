from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.views import View
from hello_django.calc.models import History


def history(request):
    sums = History.objects.order_by('-timestamp').all()[:10:-1]
    return render(request, 'calc/history.html', context={'sum': sums})


class Calc(TemplateView):

    template_name = 'calc/calc.html'

    def get_context_data(self, a, b, **kwargs):
        context = super().get_context_data(**kwargs)
        context['first_number'] = a
        context['second_number'] = b
        context['sum'] = (a + b)
        h = History(value=context['sum'])
        h.save()
        return context


class IndexView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('calc')
