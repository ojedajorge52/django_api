# Generated by Django 2.2.4 on 2019-08-30 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chart',
            name='id',
            field=models.AutoField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
