# Generated by Django 5.0 on 2024-02-05 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_alter_userinfo_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='email',
            field=models.EmailField(default='wrong@email.com', max_length=254, unique=True),
        ),
    ]
