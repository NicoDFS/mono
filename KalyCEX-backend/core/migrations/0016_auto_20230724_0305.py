# Generated by Django 3.2.19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_pair_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='withdrawalrequest',
            name='state',
            field=models.IntegerField(choices=[(0, 'Created'), (1, 'Pending'), (2, 'Completed'), (3, 'Failed'), (4, 'Cancelled'), (5, 'Verifying'), (6, 'Unknown')], default=0),
        ),
    ]
