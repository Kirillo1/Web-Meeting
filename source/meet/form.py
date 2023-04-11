from django import forms

from meet.models import Questionnaire


class QuestionnaireForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Ваше имя'}),
        required=True
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Ваша фамилия'}),
        required=True
    )
    images = forms.ImageField(

    )
    family_status = forms.ChoiceField(
        widget=forms.Select(),
        choices=Questionnaire.family_status_choices
    )
    children = forms.ChoiceField(
        widget=forms.Select(),
        choices=Questionnaire.children_status
    )
    city = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Город'}),
        required=True
    )
    life_with_mom = forms.ChoiceField(
        widget=forms.Select(),
        required=True,
        choices=Questionnaire.life_with_mom_choice

    )
    addictions = forms.ChoiceField(
        widget=forms.Select(),
        required=True,
        choices=Questionnaire.addictions_choice

    )
    date_of_birthday = forms.DateInput(
    )
    height = forms.IntegerField(
        widget=forms.NumberInput(attrs={'placeholder': ' Рост'}),
        required=True
    )
    taboo = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Табу'}),
        required=True
    )
    dating = forms.ChoiceField(
        widget=forms.Select(),
        required=True,
        choices=Questionnaire.dating_choice

    )
    hobbies = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Хобби'}),
        required=True
    )
    zodiac_sign = forms.ChoiceField(
        widget=forms.Textarea(attrs={'placeholder': 'Знак зодиака'}),
        required=True,
        choices=Questionnaire.zodiac_choice

    )
    gender = forms.ChoiceField(
        widget=forms.Textarea(attrs={'placeholder': 'Пол'}),
        choices=Questionnaire.gander_choice,
        required=True
    )
    about_me = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'О себе'}),
        required=True
    )

    class Meta:
        model = Questionnaire
        fields = ('name', 'last_name', 'date_of_birthday', 'images', 'city',
                  'family_status', 'children', 'life_with_mom', 'addictions',
                  'zodiac_sign', 'height', 'dating', 'taboo', 'gender',
                  'hobbies', 'about_me',
                  )
