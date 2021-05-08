from django.db import models

class Song(models.Model):
    id = models.IntegerField(null=False, unique=True, primary_key=True)
    song_name = models.CharField(null=False, max_length=100)
    duration_in_seconds=models.IntegerField(null=False)
    uploaded_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.song_name


class Podcast(models.Model):
    id = models.IntegerField(null=False, unique=True, primary_key=True)
    podcast_name = models.CharField(null=False, max_length=100)
    duration_in_seconds=models.IntegerField(null=False)
    uploaded_time=models.DateTimeField(auto_now_add=True)
    host=models.CharField(null=False, max_length=100)
    participant=models.TextField(null=True)

    def __str__(self):
        return self.podcast_name



class Audiobook(models.Model):
    id = models.IntegerField(null=False, unique=True, primary_key=True)
    title = models.CharField(null=False, max_length=100)
    author = models.CharField(null=False, max_length=100)
    narrator = models.CharField(null=False, max_length=100)
    duration_in_seconds=models.IntegerField(null=False)
    uploaded_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title