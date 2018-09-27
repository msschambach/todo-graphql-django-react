import graphene
from applications.todo.api import todo_schema


class Query(todo_schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
