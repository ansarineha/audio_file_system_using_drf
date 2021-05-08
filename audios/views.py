from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .serializers import SongSerializer, PodcastSerializer, AudiobookSerializer
from .models import Song, Podcast, Audiobook
from rest_framework import status
from rest_framework.response import Response
from . import models, serializers



class ListAudioFileAPIView(ListAPIView):
    def get_serializer_class(self):
        return getattr(serializers, self.kwargs['audioFileType'].capitalize()+'Serializer')

    def get_queryset(self):
        table_name = self.kwargs['audioFileType'].capitalize()
        model = getattr(models, table_name)
        queryset = model.objects.all()
        return queryset

class ListOneAudioFileAPIView(ListAPIView):
    def get_serializer_class(self):
        return getattr(serializers, self.kwargs['audioFileType'].capitalize()+'Serializer')

    def get_queryset(self):
        table_name = self.kwargs['audioFileType'].capitalize()
        model = getattr(models, table_name)
        queryset = model.objects.filter(id=self.kwargs['pk'])
        return queryset


class CreateAudioFileAPIView(CreateAPIView):
    def get_serializer_class(self):
        return getattr(serializers, self.kwargs['audioFileType'].capitalize()+'Serializer')

    def get_queryset(self):
        table_name = self.kwargs['audioFileType'].capitalize()
        model = getattr(models, table_name)
        queryset = model.objects.all()
        return queryset

    def create(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"message":"Action is successful"}, status=status.HTTP_201_CREATED)
        return Response(data={"message":"The request is invalid"}, status=status.HTTP_400_BAD_REQUEST)

    

class UpdateAudioFileAPIView(UpdateAPIView):
    def get_serializer_class(self):
        return getattr(serializers, self.kwargs['audioFileType'].capitalize()+'Serializer')

    def get_queryset(self):
        table_name = self.kwargs['audioFileType'].capitalize()
        model = getattr(models, table_name)
        queryset = model.objects.all()
        return queryset

        
    def update(self, request, *args, **kwargs):
        partial=kwargs.pop('partial', False)
        instance=self.get_object()
        serializer=self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(data={"message":"Action is successful"}, status=status.HTTP_201_CREATED)
        return Response(data={"message":"The request is invalid"}, status=status.HTTP_400_BAD_REQUEST)



class DeleteAudioFileAPIView(DestroyAPIView):
    def get_serializer_class(self):
        return getattr(serializers, self.kwargs['audioFileType'].capitalize()+'Serializer')

    def get_queryset(self):
        table_name = self.kwargs['audioFileType'].capitalize()
        model = getattr(models, table_name)
        queryset = model.objects.filter(id=self.kwargs['pk'])
        return queryset

    def destroy(self, request, *args, **kwargs):
        instance = self.get_queryset()
        if instance.exists():
            return Response(data={"message":"Action is successful"}, status=status.HTTP_201_CREATED)
        elif not instance.exists():
            return Response(data={"message":"The request is invalid"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(data={"message":"Any other error occured"}, status=status.HTTP_400_BAD_REQUEST)

