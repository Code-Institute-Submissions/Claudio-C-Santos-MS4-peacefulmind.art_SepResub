# Generated by Django 3.2 on 2021-06-30 10:46

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('email', models.CharField(max_length=254)),
                ('street_address1', models.CharField(max_length=80)),
                ('street_address2', models.CharField(blank=True, max_length=80, null=True)),
                ('town_or_city', models.CharField(max_length=40)),
                ('postcode', models.CharField(max_length=20)),
                ('county', models.CharField(blank=True, max_length=80, null=True)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('material', models.CharField(blank=True, max_length=254, null=True)),
                ('color', models.CharField(blank=True, max_length=254, null=True)),
                ('jewel_type', models.CharField(choices=[('Pendant', 'Pendant'), ('Ring', 'Ring'), ('Other', 'Other')], default='Other', max_length=10)),
                ('notes', models.TextField()),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
