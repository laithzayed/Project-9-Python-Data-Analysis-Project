# Generated by Django 3.1.7 on 2021-03-25 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstOne', '0009_auto_20210325_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
