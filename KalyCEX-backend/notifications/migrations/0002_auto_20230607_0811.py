# Generated by Django 3.2.18 

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='users',
            field=models.ManyToManyField(related_name='mailing', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='notification',
            name='users',
            field=models.ManyToManyField(related_name='notifications', to=settings.AUTH_USER_MODEL),
        ),
    ]