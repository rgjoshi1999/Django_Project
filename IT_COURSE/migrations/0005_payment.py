# Generated by Django 5.0.1 on 2024-02-22 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IT_COURSE', '0004_remove_contactus_message_alter_contactus_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('card_number', models.CharField(max_length=10)),
                ('exp_month', models.IntegerField()),
                ('exp_year', models.IntegerField()),
                ('cvc', models.IntegerField()),
            ],
        ),
    ]