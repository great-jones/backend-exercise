import graphene
from graphene import Connection, Int
from graphene_django import DjangoObjectType

from comments.models import Comment


class CommentType(DjangoObjectType):
    class Meta:
        model = Comment
        fields = ('text', 'author', 'id')

    # graphene fields here
    text = None
    author = None
    mentions = None

    def resolve_mentions(root, info):
        return []

class CreateCommentInput(graphene.InputObjectType):
    text = graphene.String(required=True)

class CreateCommentResponse(graphene.ObjectType):
    comment = graphene.Field(CommentType)


class CreateComment(graphene.Mutation):
    class Arguments:
        input = CreateCommentInput(required=True)

    comment = graphene.Field(lambda: CommentType)
    Output = CreateCommentResponse

    def mutate(self, info, input):
        """
        - extract from the input.text a list of all users who were @mentioned
        - for each @mention, create and insert a Mention (which just joins Comment to User) into DB
        - return a CreateCommentResponse with the comment
        """

class Mutation(graphene.ObjectType):
    create_comment = CreateComment.Field()