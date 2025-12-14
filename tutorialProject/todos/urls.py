from django.urls import path

from . import views

urlpatterns = [
    path("hello", views.hello_world_view, name="hello_world"),
    path("", views.hello_python_view, name="hello_python"),
    path("temp", views.hello_html_view, name="hello_html"),
    path("redirect", views.other_view, name="other_view"),
    path("user", views.post_example, name="post_method"),
    path("submit", views.submit_exemple, name="submit_exemple"),
    path("form", views.submit_django_form, name="django_form"),
    path("temp2", views.temp_view, name="temp_view"),
    path("todos", views.todos_view, name="todos"),
    path("person/<int:person_id>", views.person_details, name="person"),
    path("delete_todo/<int:todo_id>", views.delete_todo, name="delete_todo"),
    path("toggle_todo/<int:todo_id>", views.toggle_todo_done, name="toggle_todo"),
    path("path/<str:name>", views.hello_path, name="path_html"),
]
