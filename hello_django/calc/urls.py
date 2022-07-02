from django.urls import path
from hello_django.calc import views


urlpatterns = [
    path('', views.IndexView.as_view()),
    path(
        '<int:a>/<int:b>/',
        views.Calc.as_view(),
        name='calc'
    ),
    path('history/', views.history),
]
