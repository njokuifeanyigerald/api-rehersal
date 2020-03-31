from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import PostSerializer,ViewModelSerializer
from .models import Post
from rest_framework.permissions import AllowAny,IsAuthenticatedOrReadOnly,IsAdminUser,IsAuthenticated
from rest_framework import generics,mixins,viewsets





class ViewClass(viewsets.ModelViewSet):
    serializer_class = ViewModelSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly,]


class Generics(
    mixins.CreateModelMixin,mixins.ListModelMixin,
    
    generics.GenericAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    def get(self, request, *args,**kwargs):
        return self.list( request, *args,**kwargs)
    def post(self, request, *args,**kwargs):
        return self.create(request, *args,**kwargs)
    

class UpdateRetrieveDelete(
    mixins.DestroyModelMixin,mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin, generics.GenericAPIView):

    serializer_class = PostSerializer
    queryset = Post.objects.all()
    # lookup_field = "id"

    def put(self, request, *args,**kwargs):
        return self.update(request,*args,**kwargs)
    def put(self, request, *args,**kwargs):
        return self.partial_update(request,*args,**kwargs)
    def delete(self, request, *args,**kwargs):
        return self.destroy(request,*args,**kwargs)





class Home(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    def get(self, request, *args,**kwargs):
        qs = Post.objects.all()
        # post = qs.first()
        serializer = PostSerializer(qs, many=True)
        # serializer = PostSerializer(post)
        return Response(serializer.data)

    def post(self, request, *args,**kwargs):
        serializer = PostSerializer(qs=request.data)
        serializer.save()
        return Response(serializer.data)
        # return Response(serializer.errors)

    