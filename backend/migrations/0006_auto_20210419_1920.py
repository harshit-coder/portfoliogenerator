# Generated by Django 3.0.10 on 2021-04-19 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_auto_20210419_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certification',
            name='img3',
            field=models.ImageField(null=True, upload_to='images/', verbose_name='Do you want Set a  image'),
        ),
        migrations.AlterField(
            model_name='internships',
            name='c_img1',
            field=models.ImageField(null=True, upload_to='images/', verbose_name='Do you want to upload a image'),
        ),
        migrations.AlterField(
            model_name='intro',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Set a portfolio image'),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='c_img2',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='img7',
            field=models.ImageField(null=True, upload_to='images/', verbose_name='Do you want Set a  image'),
        ),
    ]
