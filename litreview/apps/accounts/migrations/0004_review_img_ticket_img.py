# Generated by Django 4.0.1 on 2022-02-22 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_userfollow_user_to_add'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='img',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='img',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]