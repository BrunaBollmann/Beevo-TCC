# Generated by Django 4.1.1 on 2022-09-12 19:09

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('agendamento', '0004_alter_responsavel_telefone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='responsavel',
            name='telefone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True),
        ),
    ]
