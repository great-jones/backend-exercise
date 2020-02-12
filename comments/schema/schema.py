from graphene import Schema
from graphene import ObjectType
import comments.schema as comment_schema


class Mutation(comment_schema.Mutation):
    pass

SCHEMA = Schema(mutation=Mutation)