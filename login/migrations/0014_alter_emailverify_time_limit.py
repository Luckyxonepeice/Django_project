# Generated by Django 5.0 on 2024-02-07 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0013_alter_emailverify_user_verify'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverify',
            name='time_limit',
            field=models.DateTimeField(),
        ),
    ]
