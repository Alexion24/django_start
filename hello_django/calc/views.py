from django.http import HttpResponse
from django.views import View


def index(request, a=0, b=0):
    return HttpResponse(f'{a} + {b} = {a + b}')


class IndexView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('calc')

