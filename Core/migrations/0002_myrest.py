# Generated by Django 2.2.12 on 2022-04-14 05:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('food', '0003_auto_20220306_0618'),
        ('Core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyRest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rest', models.ManyToManyField(to='food.Restaurants')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
