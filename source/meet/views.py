from django.shortcuts import render
from .models import Questionnaire


def index(request):
    context = {}
    questionnaires = Questionnaire.objects.all()
    context = {
        'questionnaires': questionnaires
    }
    return render(request, 'index.html', context=context)
