# Generated by Django 2.1.5 on 2020-03-19 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='rsa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p', models.IntegerField(max_length=120)),
                ('q', models.IntegerField(max_length=120)),
                ('e', models.IntegerField(max_length=120)),
                ('m', models.CharField(max_length=120)),
            ],
        ),
    ]