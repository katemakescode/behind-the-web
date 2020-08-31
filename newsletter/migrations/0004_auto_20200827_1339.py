# Generated by Django 3.1 on 2020-08-27 01:39

from django.db import migrations
import django.utils.timezone
import newsletter.models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0003_auto_20200820_0327'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscriber',
            name='email_address',
        ),
        migrations.AddField(
            model_name='subscriber',
            name='email',
            field=newsletter.models.LCEmailField(default=django.utils.timezone.now, max_length=254, unique=True),
            preserve_default=False,
        ),
    ]