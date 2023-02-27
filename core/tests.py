from django.test import TestCase
from django.contrib.auth import get_user_model

from core.models import Note


class First(TestCase):

    def setUp(self):
        user = get_user_model().objects.create(username='username', password='password')
        Note.objects.create(headline="Note 1", content="This is a test content", user=user)

    def test_note_text(self):
        note = Note.objects.get(headline="Note 1")
        self.assertEqual(note.content, "This is a test content")