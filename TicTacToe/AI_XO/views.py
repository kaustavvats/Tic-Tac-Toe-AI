from django.shortcuts import render, redirect
from .utils import get_value


def index(request):
    return redirect('name')


def enter_name(request):
    args = {
        'error': False,
        'mssg': "",
    }
    if request.method != 'POST':
        return render(request, 'AI_XO/name.html', args)
    else:
        nick_name = get_value(request.POST, 'nick')
        print("Nick: %s" % nick_name)
        if nick_name == "":
            args['error'] = True
            args['mssg'] = "Please Enter a Nick"
            return render(request, 'AI_XO/name.html', args)
        args['error'] = False
        args['mssg'] = ""
        return redirect('main')


def lets_play(request):
    return render(request, 'AI_XO/main.html')

