from django.urls import path
from .views import ListAudioFileAPIView, ListOneAudioFileAPIView, CreateAudioFileAPIView, UpdateAudioFileAPIView, DeleteAudioFileAPIView


urlpatterns = [
    path("<str:audioFileType>/", ListAudioFileAPIView.as_view(), name="list"),
    path("<str:audioFileType>/<int:pk>/", ListOneAudioFileAPIView.as_view(), name="list1"),
    path("create/<str:audioFileType>/", CreateAudioFileAPIView.as_view(), name="create"),
    path("update/<str:audioFileType>/<int:pk>/", UpdateAudioFileAPIView.as_view(), name="update"),
    path("delete/<str:audioFileType>/<int:pk>/", DeleteAudioFileAPIView.as_view(), name="delete"),
]
