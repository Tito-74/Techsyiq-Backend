# Generated by Django 4.2 on 2023-04-09 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone_no', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('module', models.CharField(max_length=255)),
                ('starting_date', models.CharField(choices=[('2ND Feb', '2ND Feb'), ('8th Aug', '8th Aug'), ('9th Nov', '9th Nov')], default='2ND Feb', max_length=255)),
            ],
        ),
    ]
