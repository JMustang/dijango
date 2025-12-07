from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import redirect, render
from .forms import PersonForm


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


def post_example(request):
    if request.method == "POST":
        form = PersonForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data["name"]
            age = form.cleaned_data["age"]
            job = form.cleaned_data["job"]

            return HttpResponse(f"Nome: {name}, idade: {age}, profissão: {job}")
    else:
        return HttpResponseNotAllowed(["POST"])


def submit_exemple(request):
    return render(request, "todos/submit.html")


def submit_django_form(request):
    form = PersonForm()
    return render(request, "todos/submit_django_form.html", {"form": form})
