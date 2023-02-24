import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.urls import reverse_lazy

from core.forms import NoteForm
from core.models import Note


class Login(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    next_page = reverse_lazy('index')

class Logout(LoginRequiredMixin, LogoutView):
    next_page = reverse_lazy('login')
    login_url = reverse_lazy('login')

class NoteList(LoginRequiredMixin, View):
    def get(self, request):
        return JsonResponse({'notes': list(request.user.notes.all().order_by('-id').values())})


class AddNote(LoginRequiredMixin, View):
    def post(self, request):
        headline = request.POST.get('headline')
        content = request.POST.get('content')
        note = Note(headline=headline, content=content, user=request.user)
        note.save()
        response_data = {
            'id': note.id,
            'user': note.user.username,
            'headline': note.headline,
            'content': note.content,
            
        }
        return HttpResponse(json.dumps(response_data), content_type="application/json")


