# Generated by Django 2.1.5 on 2020-03-19 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='elgamalre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pr', models.IntegerField()),
                ('m', models.IntegerField()),
                ('rand1', models.IntegerField()),
                ('rand2', models.IntegerField()),
            ],
        ),
    ]