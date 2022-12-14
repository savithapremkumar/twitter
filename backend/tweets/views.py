from rest_framework.viewsets import ModelViewSet
from .models import Tweet
from .serializers import TweetSerializer


class TweetsViewSet(ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
