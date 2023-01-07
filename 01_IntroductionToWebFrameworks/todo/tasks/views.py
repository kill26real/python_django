from django.http import HttpResponse

from django.views import View


class ToDoView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('<p><b>Список дел на день:</b></p>'
                            '<ul>'
                            '<li>Проснуться</li>'
                            '<li>Покодить</li>'
                            '<li>Лечь спать</li>'
                            '</ul>')
