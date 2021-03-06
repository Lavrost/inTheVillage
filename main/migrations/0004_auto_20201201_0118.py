# Generated by Django 3.1.3 on 2020-11-30 22:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20201130_1725'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория(ю)', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='object',
            options={'ordering': ['title'], 'verbose_name': 'Объект', 'verbose_name_plural': 'Объекты'},
        ),
        migrations.AlterField(
            model_name='category',
            name='house',
            field=models.CharField(choices=[('Весь дом', 'Весь дом'), ('Часть дома', 'Часть дома'), ('Участок', 'Участок'), ('Таунхаус', 'Таунхаус')], default='Весь дом', max_length=50),
        ),
        migrations.AlterField(
            model_name='object',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='object',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='object',
            name='square',
            field=models.PositiveIntegerField(verbose_name='Площадь'),
        ),
        migrations.AlterField(
            model_name='object',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Заголовок'),
        ),
    ]
