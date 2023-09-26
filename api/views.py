from django.shortcuts import render
from rest_framework import generics
from .models import Note
from .serializers import NoteSerializer
# Create your views here.

class NoteList(generics.ListCreateAPIView):
    queryset=Note.objects.all() # Retrieve all note
    serializer_class=NoteSerializer

note_list_view=NoteList.as_view()

# For destoying ||  for deleting data

class NoteUpdateDestroyData(generics.RetrieveUpdateDestroyAPIView):
    queryset=Note.objects.all()
    serializer_class=NoteSerializer

note_update_delete=NoteUpdateDestroyData.as_view()



