# Generated by Django 4.1.1 on 2022-09-12 18:54

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('agendamento', '0002_sala_alter_agendamento_equipamento_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='responsavel',
            name='materia',
        ),
        migrations.AddField(
            model_name='responsavel',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='responsavel',
            name='telefone',
            field=phone_field.models.PhoneField(default='teste', max_length=31),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Materia',
        ),
    ]
