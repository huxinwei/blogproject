# Generated by Django 3.1.2 on 2020-11-03 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201102_2129'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_time'], 'verbose_name': '文章', 'verbose_name_plural': '文章'},
        ),
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
    ]
