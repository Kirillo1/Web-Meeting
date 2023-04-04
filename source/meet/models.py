from django.db import models


class Questionnaire(models.Model):
    family_status_choices = [
        ('single', 'Холост'), ('divorced', 'Разведен'),
        ('actively_looking', 'В активном поиске'), ('married', 'В браке')
    ]
    children_status = [
        ('yes', 'Да'), ('no', 'Нет')
    ]
    life_with_mom_choice = [
        ('yes', 'Да'), ('no', 'Нет'),
        ('with_me', 'Мама живет со мной')
    ]
    addictions_choice = [
        ('smoking', 'Курение'), ('alcohol', 'Алкоголь'),
        ('gambling', 'Лудомания')
    ]
    dating_choice = [
        ('hookup', 'Одна встреча'), ('meetings', 'Регулярные встречи'),
        ('relationships', 'Серьезные отношения'), ('communication', 'Общение')
    ]
    zodiac_choice = [
        ('Capricorn', 'Козерог'), ('Aquarius', 'Водолей'),
        ('Pisces', 'Рыбы'), ('Aries', 'Овен'), ('Taurus', 'Телец'),
        ('Gemini', 'Близнецы'), ('Cancer', 'Рак'), ('Leo', 'Лев'),
        ('Virgo', 'Дева'), ('Libra', 'Весы'), ('Scorpio', 'Скорпион'),
        ('Ophiuchus', 'Змееносец'), ('Sagittarius', 'Стрелец')
    ]
    gander_choice = [
        ('w', 'ж'), ('m', 'м')
    ]
    name = models.CharField(
        max_length=50, verbose_name="Имя",
        null=False, blank=False
    )
    last_name = models.CharField(
        max_length=50, verbose_name="Фамилия",
        null=False, blank=False
    )
    images = models.ImageField(
        verbose_name="Фотография", upload_to='uploads/',
        null=False, blank=False
    )
    family_status = models.CharField(
        max_length=50, verbose_name='Семейное положение',
        choices=family_status_choices
    )
    children = models.CharField(
        max_length=50, verbose_name='Наличие детей',
        choices=children_status
    )
    city = models.CharField(
        max_length=50, verbose_name="Город",
        null=False, blank=False
    )
    life_with_mom = models.CharField(
        max_length=50, verbose_name="Живешь ли ты с мамой?",
        choices=life_with_mom_choice
    )
    addictions = models.CharField(
        max_length=50, verbose_name="Вредные привычки",
        choices=addictions_choice
    )
    date_of_birthday = models.DateField(
        verbose_name="Дата рождения"
    )
    height = models.PositiveIntegerField(
        verbose_name="Рост"
    )
    taboo = models.TextField(
        max_length=1000, verbose_name='Табу'
    )
    dating = models.CharField(
        max_length=100, verbose_name="Цель знакомств",
        choices=dating_choice
    )
    hobbies = models.TextField(
        max_length=1000, verbose_name='Увлечения'
    )
    zodiac_sign = models.CharField(
        max_length=100, verbose_name="Знак зодиака",
        choices=zodiac_choice
    )
    gender = models.CharField(
        max_length=100, verbose_name="Пол",
        choices=gander_choice
    )
    about_me = models.TextField(
        max_length=1000, verbose_name='Обо мне...'
    )

    class Meta:
        verbose_name = 'Анкета'
        verbose_name_plural = 'Анкеты'
