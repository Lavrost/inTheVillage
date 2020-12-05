from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField


class Category(models.Model):
    """Выбор объекта недвижимости"""
    full = 'Весь дом'
    half = 'Часть дома'
    parcel = 'Участок'
    townhouse = 'Таунхаус'
    House_choice = [
        (full, 'Весь дом'),
        (half, 'Часть дома'),
        (parcel, 'Участок'),
        (townhouse, 'Таунхаус'),
    ]
    house = models.CharField(max_length=50, default=full, choices=House_choice)

    def __str__(self):
        return self.house

    class Meta:
        verbose_name = 'Категория(ю)'
        verbose_name_plural = 'Категории'


class User(models.Model):
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    email = models.EmailField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(unique=True, max_length=30)
    password = models.CharField(max_length=50)
    dateRegistration = models.DateField(auto_now_add=True, auto_now=False, verbose_name='Дата регистрации')

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['username']


# ПЕРЕИМЕНУЙ
class RealtyObject(models.Model):
    """Сам объект недвижимости"""
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    description = models.TextField(verbose_name='Описание')
    slug = models.SlugField(verbose_name='URL', unique=True)
    views = models.IntegerField(default=0, verbose_name='Просмотры')
    photos = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фотографии')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Изменено')
    # author = models.ForeignKey(User)
    square = models.FloatField(verbose_name='Площадь')
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Объект'
        verbose_name_plural = 'Объекты'
        ordering = ['title']

    def get_url(self):
        return reverse('realty', args=[self.slug])


'''
Objects
=======
    Title(CharField)            +
    Photos(ImageField)          +
    Place(CharField(?))         -
    Square(FloatField)          +
    Description(TextField)      +
    DateTimeAdd(DateTimeField)  +
    Category(ForeignKey)        +
    Author()                    +
    Views(IntegerField)         +
    Slug(SlugField6yt)          +
    
User(админ, юзер, модератор, риэлтор)
=======
    Status(Choice)              -
    Phone(PhoneField)           +
    E-mail(EmailField)          +
    Name(CharField)             +
    Password(PasswordField)     +-
    Username(CharField)         +
    DateRegistration(DateField) +
    
'''
