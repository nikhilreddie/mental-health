# Generated by Django 4.1.5 on 2024-04-07 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_doctor_customuser_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emotions',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('username', models.CharField(max_length=100)),
                ('emotionname', models.CharField(max_length=100)),
            ],
        ),
    ]
