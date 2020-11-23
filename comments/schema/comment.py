import re

import graphene
from django.contrib.auth.models import User
from graphene import Connection, Int
from graphene_django import DjangoObjectType

from comments import email_service
from comments.models import Comment, Mention
from comments.schema.mention import MentionType
from comments.schema.user import UserType


class CommentType(DjangoObjectType):
    class Meta:
        model = Comment
        fields = ('text', 'id')

    text = graphene.NonNull(graphene.String)
    mentions = graphene.List(MentionType)

    def resolve_mentions(root, info, **kwargs):
        return Mention.objects.filter(comment_id=root.id)


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
        '''
        Goal #1 is to parse @mentions in the comment text and send a notification email to the mentioned user.
        For the email, you can use email_service.send_email(email_address, comment_id). You do not need to implement
        the actual email sending functionality.

        Note that usernames contain any characters a-z (uppercase or lowercase), digits as well as "." (periods)

        Goal #2 now that we are able to send notifications for mentions, we need to enable the frontend to know about the
        mentions that exist in each comment. To do this, you'll need to create a Django model for a join table that joins
        users to comments. Create the Django model and then the corresponding GraphQL type.
        Once the Mention type is created, add a field for list of mentions to the Comment schema and add a resolver for it.
        '''
        pattern = '@[a-zA-Z.\d]*'
        comment = Comment.objects.create(text=input.text)
        mentions = re.findall(pattern, input.text)
        for mention in mentions:
            username = mention[1:]
            user = User.objects.get(username=username)
            email_service.send_email(user.email, comment.id)
            Mention.objects.create(user=user, comment=comment)
        for comment in Comment.objects.all():
            print(f'this is a comment from the DB: {comment}')


        return CreateCommentResponse(comment=comment)




class Mutation(graphene.ObjectType):
    create_comment = CreateComment.Field()

class Query(object):

    comment = graphene.Field(
        CommentType,
        id=graphene.NonNull(graphene.Int),
    )

    def resolve_comment(self, info, **kwargs):
        comment_id = kwargs.get('id')
        return Comment.objects.get(id=comment_id)
