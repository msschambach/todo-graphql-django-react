from django.contrib import admin
from django.urls import path, include
from graphene_django.views import GraphQLView
from applications.todo import urls as todo_urls
from applications.todo.api import schema

urlpatterns = [
    path("admin/", admin.site.urls),
    path("graphql/", GraphQLView.as_view(graphiql=True, schema=schema)),
    path("", include(todo_urls)),
]
