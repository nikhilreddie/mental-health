# Generated by Django 4.1.5 on 2024-03-19 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_customuser_mobile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('doctorId', models.AutoField(primary_key=True, serialize=False)),
                ('doctorName', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255)),
                ('hospitalName', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('mobileNumber', models.CharField(max_length=15)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='city',
            field=models.CharField(default='', max_length=100),
        ),
    ]
