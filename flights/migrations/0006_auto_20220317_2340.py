# Generated by Django 2.2.12 on 2022-03-17 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0005_auto_20220317_2333'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='times',
            name='time',
            field=models.TimeField(),
        ),
        migrations.AddField(
            model_name='flights',
            name='dates',
            field=models.ManyToManyField(to='flights.Dates'),
        ),
    ]
