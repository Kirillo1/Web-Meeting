from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Questionnaire
from .form import QuestionnaireForm


def index(request):
    context = {}
    questionnaires = Questionnaire.objects.all()
    context = {
        'questionnaires': questionnaires
    }
    return render(request, 'index.html', context=context)


def create_meet(request):
    context = {}
    if request.method == 'POST':
        meet_forms = QuestionnaireForm(request.POST)
        if meet_forms.is_valid():
            questionnaire = meet_forms.save()
        return HttpResponseRedirect(reverse('meet:index'))
    else:
        meet_forms = QuestionnaireForm()

    context = {
        'meet_forms': meet_forms
    }

    return render(request, 'create_meet.html', context=context)
