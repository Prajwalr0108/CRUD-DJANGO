# Generated by Django 3.0.8 on 2021-07-24 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BasicDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=100)),
                ('Last_Name', models.CharField(max_length=50)),
                ('Father_Name', models.CharField(max_length=50)),
                ('Mother_Name', models.CharField(max_length=50)),
                ('Date_of_birth', models.DateField()),
                ('Gender', models.CharField(max_length=10)),
                ('About', models.TextField()),
            ],
        ),
    ]
