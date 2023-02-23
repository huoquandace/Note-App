import json
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.urls import reverse_lazy

from core.forms import NoteForm
from core.models import Note


class Home(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')
    def get(self, request):
        return render(request, 'index.html', {
        'notes': request.user.notes.all().order_by('-id'),
        'form': NoteForm(),
    })

class Login(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    next_page = reverse_lazy('index')

class Logout(LoginRequiredMixin, LogoutView):
    next_page = reverse_lazy('login')
    login_url = reverse_lazy('login')

def add_note(request):
    if request.method == 'POST':
        headline = request.POST.get('headline')
        content = request.POST.get('content')

        note = Note(headline=headline, content=content, user=request.user)
        note.save()

        response_data = {
            'result': 'Add note successfully!',
            'id': note.id,
            'user': note.user.username,
            'headline': note.headline,
            'content': note.content,
            
        }

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )