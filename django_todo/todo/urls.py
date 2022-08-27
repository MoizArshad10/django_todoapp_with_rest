from django.urls import path
from todo import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path("",views.ListTodoAPIVIEW.as_view(),name="todo_list"),
    path("create/", views.CreateTodoAPIVIEW.as_view(),name="todo_create"),
    path("update/<int:pk>/",views.UpdateTodoAPIVIEW.as_view(),name="update_todo"),
    path("delete/<int:pk>/",views.DeleteTodoAPIVIEW.as_view(),name="delete_todo")
]