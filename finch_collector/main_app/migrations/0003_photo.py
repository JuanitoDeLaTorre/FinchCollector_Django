# Generated by Django 4.1.7 on 2023-03-30 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_camera_image_camera_name_camera_price_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('url', models.CharField(default='', max_length=250)),
                ('camera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.camera')),
            ],
        ),
    ]
