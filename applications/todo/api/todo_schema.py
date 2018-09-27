import graphene
from graphene_django.types import DjangoObjectType
from applications.todo.models import List, Task


class TaskType(DjangoObjectType):
    class Meta:
        model = Task


class ListType(DjangoObjectType):
    tasks = graphene.List(TaskType)

    class Meta:
        model = List

    def resolve_tasks(self, info, **kwargs):
        return Task.objects.filter(list=self)


class Query(graphene.ObjectType):
    lists = graphene.List(ListType)
    tasks = graphene.List(TaskType)

    def resolve_lists(self, info, **kwargs):
        return List.objects.all()

    def resolve_tasks(self, info, **kwargs):
        return Task.objects.all()
