# Generated by Django 3.1.7 on 2021-08-12 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentor', '0003_regi_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logi',
            name='status',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='regi',
            name='phone',
            field=models.IntegerField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='regi',
            name='status',
            field=models.CharField(default='', max_length=10),
        ),
    ]