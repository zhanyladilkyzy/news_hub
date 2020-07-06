from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from .serializers import MainUserSerializer, MainUserSerializer2, \
    NewsSerializer, CategorySerializer
from .models import MainUser, Category, News
from .token import get_token


@api_view(['POST'])
def create_user(request):
    serializer = MainUserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = MainUser.objects.create_user(username=request.data['username'],
                                        full_name=request.data['full_name'],
                                        password=request.data['password'])
    token = get_token(user)
    serializer2 = MainUserSerializer2(user)
    return Response({'token': token, 'user': serializer2.data})


@api_view(['GET'])
def get_all_users(request):
    users = MainUser.objects.all()
    serializer = MainUserSerializer2(users, many=True)
    return Response(serializer.data)


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticated,)


class NewsViewSet2(viewsets.ReadOnlyModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsViewSet3(viewsets.GenericViewSet, mixins.CreateModelMixin,
                  mixins.ListModelMixin):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    @action(methods=['GET'], detail=True)
    def get_news_by_id(self, request, pk):
        news = News.objects.get(id=pk)
        serializer = NewsSerializer(news)
        return Response(serializer.data)