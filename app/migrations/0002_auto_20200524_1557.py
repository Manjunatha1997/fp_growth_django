# Generated by Django 3.0.3 on 2020-05-24 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='chicken',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='eggs',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='ginger',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='masala',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='oil',
            field=models.CharField(max_length=100),
        ),
    ]