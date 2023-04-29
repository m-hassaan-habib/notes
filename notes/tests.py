from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Note

class NoteTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.note_data = {'title': 'Test Note', 'content': 'Test Content'}
        self.note = Note.objects.create(**self.note_data)
        self.url = reverse('note-retrieve-update-delete', kwargs={'pk': self.note.id})

    def test_create_note(self):
        response = self.client.post(reverse('note-list-create'), self.note_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Note.objects.count(), 2)

    def test_read_notes(self):
        response = self.client.get(reverse('note-list-create'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_read_single_note(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.note_data['title'])

    def test_update_note(self):
        updated_data = {'title': 'Updated Test Note', 'content': 'Updated Test Content'}
        response = self.client.put(self.url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Note.objects.get(id=self.note.id).title, updated_data['title'])

    def test_delete_note(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Note.objects.count(), 0)
