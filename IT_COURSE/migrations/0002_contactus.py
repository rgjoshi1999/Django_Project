# Generated by Django 5.0.1 on 2024-02-03 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IT_COURSE', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('mobile_number', models.IntegerField()),
                ('message', models.CharField(max_length=20)),
            ],
        ),
    ]
