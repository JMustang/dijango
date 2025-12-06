from django.http import HttpResponse
from django.shortcuts import redirect, render


# Create your views here.
def hello_world_view(request):
    return HttpResponse("Hello World! 🖖🏻")


def hello_python_view(request):
    return HttpResponse("Hello Python! 🐍🖖🏻")


def hello_html_view(request):
    return render(request, "todos/hello.html")


def hello_path(request, name):
    return HttpResponse(f"Hello {name}!!🖖🏻")


def other_view(request):
    return redirect("hello_html")
