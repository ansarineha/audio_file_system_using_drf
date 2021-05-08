from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Song
from .serializers import SongSerializer



class ListSongAPITest(APITestCase):
    def test_list_song_api(self):
        response = self.client.get('/song/', format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)

class ListPodcastAPITest(APITestCase):
    def test_list_podcast_api(self):
        response = self.client.get('/podcast/', format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)


class ListAudiobookAPITest(APITestCase):
    def test_list_podcast_api(self):
        response = self.client.get('/audiobook/', format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)


class CreateSongAPITest(APITestCase):
    def test_create_song_api(self):
        data = {'id':1,'song_name':'attention','duration_in_seconds':120}
        response = self.client.post('/create/song/', data, format='json')
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)


class CreatePodcastAPITest(APITestCase):
    def test_create_song_api(self):
        data = {'id':1,'podcast_name':'weekend','duration_in_seconds':20,'host':'localhost'}
        response = self.client.post('/create/podcast/', data, format='json')
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)


