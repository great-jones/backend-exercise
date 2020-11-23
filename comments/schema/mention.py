from graphene_django import DjangoObjectType

from comments.models import Mention


class MentionType(DjangoObjectType):
    class Meta:
        model = Mention
        fields = ('user', 'comment')