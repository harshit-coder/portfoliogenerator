# Generated by Django 3.0.10 on 2021-04-19 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20210419_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intro',
            name='d_o_b',
            field=models.DateField(blank=True, verbose_name='Date of Birth'),
        ),
    ]
