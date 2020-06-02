# Generated by Django 3.0.6 on 2020-06-01 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModuleLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.IntegerField()),
                ('humidity', models.IntegerField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('module_id', models.IntegerField()),
            ],
        ),
    ]
