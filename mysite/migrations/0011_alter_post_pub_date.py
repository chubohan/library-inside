# Generated by Django 4.2.6 on 2023-10-29 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0010_post_publishing_alter_post_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default='2023-10-29T10:16:56.127894+00:00'),
        ),
    ]
