# Generated by Django 4.0.4 on 2022-05-05 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handmedown', '0006_comment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
