# Generated by Django 4.2.6 on 2023-10-29 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0005_alter_post_now_alter_post_pub_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='now',
            new_name='date',
        ),
    ]
