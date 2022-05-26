#from django.shortcuts import render, get_object_or_404, redirect

from django.forms import ValidationError
from rest_framework import generics, permissions,mixins,status
from .models import Job, User,BookmarkJob
from .serializers import JobSerializer, BookSerializer

from rest_framework.exceptions import ValidationError


from rest_framework import status

from jobapp import serializers


# from jobapp.forms import *
# from jobapp.models import *
# from jobapp.permission import *

#  my class based view
class JobView(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # i have to add override function 👇
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class JobDetail(generics.RetrieveAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class JobDelete(generics.RetrieveAPIView,mixins.DestroyModelMixin):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    def delete(self,request,*args, **kwargs):
        owner = Job.objects.filter(pk=kwargs['pk'],user=self.request.user)
        if owner.exists():
            return self.destroy(request,*args, **kwargs)
        else:
            raise ValidationError('Opps 😐! You Can Only Deletes Your Job Only, ISNP Teams')




class JobUpdate(generics.RetrieveUpdateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def update(self,request,*args, **kwargs):
        owner = Job.objects.filter(pk=kwargs['pk'],user=self.request.user)
        if owner.exists():
            queryset = Job.objects.all()
        else:
            raise ValidationError('Opps 😐! You Can Only Updates Your Job Only, ISNP Teams')

class SavedJob(generics.ListCreateAPIView):
    queryset = BookmarkJob.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]




