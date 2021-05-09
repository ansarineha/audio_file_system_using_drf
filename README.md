# audio_file_system_using_drf

This is an Audio File Management System which simulates the behavior of an audio file by retreiving, adding, updating and deleting the files.

### How to run application in your system:

1. Create virtual environment in the root directory by using.
   > py -m venv env
2. Now activate the virtual environment on your system by using.
   > env/Scripts/activate
   (this should activate the virtual environment on your system)
3. Install all the dependencies.
   All the dependencies which project requires are consolidated in requirements.txt file, to install them simply use.
   > pip install -r requirements.txt
4. Now finally run the application by using following command.
   > python manage.py runserver 
   (and you should see the app in action on http://localhost:8000/)
   
   
### endpoints & inputs for checking API:
1. Listing all the files of one type:<br>
   http://127.0.0.1:8000/audioFileType/   (replace audioFileType by any audio file type i.e. song, podcast and audiobook)</br>
   
2. Retrieving particular file detail: <br>
   http://127.0.0.1:8000/audioFileType/pk/  (replace audioFileType by any audio file type i.e. song, podcast and audiobook and pk by any integer id)</br>
   
3. To create a new file type: <br>
   http://127.0.0.1:8000/create/audioFileType/ (replace audioFileType by any audio file type i.e. song, podcast and audiobook)</br>
   sample input: </br>
   { </br>
   "id":1, <br>
   "song_name":"memories", <br>
   "duration_in_seconds":120 </br>
    } </br>
   
4. To update any file type: <br>
   http://127.0.0.1:8000/update/audioFileType/pk/ (replace audioFileType by any audio file type i.e. song, podcast and audiobook and pk by any integer id)</br>
   sample input: </br>
   { </br>
   "id":1, <br>
   "song_name":"updated name", <br>
   "duration_in_seconds":120 </br>
    } </br>
   
5. To delete any file type: <br>
   http://127.0.0.1:8000/delete/audioFileType/pk/ (replace audioFileType by any audio file type i.e. song, podcast and audiobook and pk by any integer id)</br>
   
   
   
