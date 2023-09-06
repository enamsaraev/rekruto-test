from django.views import View
from django.shortcuts import render

from core.helpers import HelloHelper


class LetsBeFriends(View):
    def get(self, request, *args, **kwargs):
        data = HelloHelper(data=request.GET)
        cnt = {
            'data': data
        }

        return render(request, 'hello.html', context=cnt)