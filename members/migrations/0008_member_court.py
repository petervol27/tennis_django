# Generated by Django 5.1.1 on 2024-09-14 19:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courts', '0001_initial'),
        ('members', '0007_remove_member_trainer_delete_trainer'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='court',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='members', to='courts.court'),
        ),
    ]
