# Generated by Django 4.1.7 on 2023-03-30 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('price', models.IntegerField(default=100)),
            ],
        ),
        migrations.AddField(
            model_name='camera',
            name='gear',
            field=models.ManyToManyField(to='main_app.gear'),
        ),
    ]