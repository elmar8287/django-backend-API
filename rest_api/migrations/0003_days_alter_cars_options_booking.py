# Generated by Django 4.0.4 on 2022-08-27 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0002_cars_delete_courses'),
    ]

    operations = [
        migrations.CreateModel(
            name='Days',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('note', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Days',
            },
        ),
        migrations.AlterModelOptions(
            name='cars',
            options={'verbose_name_plural': 'Cars'},
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_api.cars')),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_api.days')),
            ],
        ),
    ]
