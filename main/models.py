from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Category(models.Model):
    """Выбор объекта недвижимости"""
    full = 'FL'
    half = 'HF'
    parcel = 'PL'
    townhouse = 'TH'
    House_choice = [
        (full, 'Весь дом'),
        (half, 'Часть дома'),
        (parcel, 'Участок'),
        (townhouse, 'Таунхаус'),
    ]
    house = models.CharField(max_length=2, default=full, choices=House_choice)


class User(models.Model):
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    email = models.EmailField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(unique=True, max_length=30)
    password = models.CharField(max_length=50)
    dateRegistration = models.DateField(auto_now_add=True, auto_now=False, verbose_name='Дата регистрации')


class Objects(models.Model):
    """Сам объект недвижимости"""
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    slug = models.SlugField(verbose_name='URL', unique=True)
    views = models.IntegerField(default=0, verbose_name='Просмотры')
    photos = models.ImageField(upload_to='photos/%Y/%m/%d/')
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Опубликовано')
    author = models.ForeignKey(User)
    square = models.PositiveIntegerField()


'''
Objects
=======
    Title(CharField)           +
    Photos(ImageField)         +
    Place(CharField(?))        -
    Square(FloatField)         +
    Description(TextField)     +
    DateTimeAdd(DateTimeField) +
    Category(ForeignKey)       +
    Author()                   +
    Views(IntegerField)        +
    Slug(SlugField6yt)         +
    
User(админ, юзер, модератор, риэлтор)
=======
    Phone(PhoneField)          +
    E-mail(EmailField)         +
    Name(CharField)            +
    Password(PasswordField)    +-
    Username(CharField)        +
    DateRegistration(DateField)+
    
'''
