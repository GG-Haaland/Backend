# Generated by Django 4.0.4 on 2022-05-05 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('handmedown', '0002_alter_post_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('item_url', models.TextField()),
                ('price', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=500)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='handmedown.post')),
            ],
        ),
    ]
