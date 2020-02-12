import graphene
from graphene import Schema
from graphene import ObjectType
import comments.schema as comment_schema


class Mutation(comment_schema.Mutation):
    pass

class Query(comment_schema.Query, graphene.ObjectType):
    pass

SCHEMA = Schema(mutation=Mutation, query=Query)