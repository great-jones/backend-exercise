import graphene
from graphene import Connection, Int
from graphene_django import DjangoObjectType

from comments.models import Comment
from comments.schema.user import UserType


class CommentType(DjangoObjectType):
    class Meta:
        model = Comment
        fields = ('text', 'id')

    text = graphene.NonNull(graphene.String)

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
        # parse mentions and send an email to the user
        for comment in Comment.objects.all():
            print(f'this is a comment from the DB: {comment}')
        comment = Comment.objects.create(text=input.text)
        return CreateCommentResponse(comment=comment)

class Mutation(graphene.ObjectType):
    create_comment = CreateComment.Field()

class Query(object):

    comment = graphene.Field(
        CommentType,
        id=graphene.NonNull(graphene.Int),
    )
