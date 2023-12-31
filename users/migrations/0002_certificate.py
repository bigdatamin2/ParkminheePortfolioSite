# Generated by Django 5.0 on 2023-12-11 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('organization', models.CharField(max_length=150)),
                ('issue_date', models.DateField()),
                ('expiration_date', models.DateField()),
            ],
        ),
    ]
