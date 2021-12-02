from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def user_input(request):
    return render(request, "base.html")


def calculator(request):
    try:
        x = request.GET['n1']
        a = int(x)
        y = request.GET['n2']
        b = int(y)
        op = request.GET['operation']
    except ValueError:
        return render(request, "base.html", {"msg": "enter valid numbers"})
    if op == 'add':
        z = a+b
        return render(request, "res.html", {"z": z})
    elif op == 'sub':
        z = a-b
        return render(request, "res.html", {"z": z})
    elif op == 'mul':
        z = a*b
        return render(request, "res.html", {"z": z})
    elif op == 'div':
        try:
            z = a/b
            return render(request, "res.html", {"z": z})
        except ZeroDivisionError:
            return HttpResponse("can not divide by zero ")