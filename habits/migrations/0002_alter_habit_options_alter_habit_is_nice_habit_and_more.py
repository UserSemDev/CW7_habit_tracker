# Generated by Django 5.0.6 on 2024-06-30 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='habit',
            options={'ordering': ['action'], 'verbose_name': 'Привычка', 'verbose_name_plural': 'Привычки'},
        ),
        migrations.AlterField(
            model_name='habit',
            name='is_nice_habit',
            field=models.BooleanField(default=False, help_text='Приятная привычка', verbose_name='Признак приятной привычки'),
        ),
        migrations.AlterField(
            model_name='habit',
            name='time',
            field=models.TimeField(help_text='Когда необходимо выполнять привычку', verbose_name='Время'),
        ),
    ]
