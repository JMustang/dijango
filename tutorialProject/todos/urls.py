from django.urls import path

from . import views

urlpatterns = [
    path("hello", views.hello_world_view, name="hello_world"),
    path("", views.hello_python_view, name="hello_python"),
    path("temp", views.hello_html_view, name="hello_html"),
    path("redirect", views.other_view, name="other_view"),
    path("user", views.post_example, name="post_method"),
    path("submit", views.submit_exemplo, name="submit_exemplo"),
    path("path/<str:name>", views.hello_path, name="path_html"),
]
