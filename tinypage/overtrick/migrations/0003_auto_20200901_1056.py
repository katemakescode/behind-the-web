# Generated by Django 3.1 on 2020-08-31 22:56

import django.utils.timezone
from django.db import migrations, models

import common.utils


class Migration(migrations.Migration):
    dependencies = [
        ('overtrick', '0002_auto_20200831_1747'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='player',
            options={'ordering': ('last_name', 'first_name')},
        ),
        migrations.AlterField(
            model_name='player',
            name='email',
            field=common.utils.LCEmailField(default=django.utils.timezone.now,
                                            max_length=254),
            preserve_default=False,
        ),
        migrations.AddConstraint(
            model_name='pair',
            constraint=models.UniqueConstraint(
                fields=('session', 'orient', 'pair_num'), name='pair_pk'),
        ),
        migrations.AddConstraint(
            model_name='player',
            constraint=models.UniqueConstraint(
                fields=('last_name', 'first_name'), name='player_pk'),
        ),
        migrations.AddConstraint(
            model_name='session',
            constraint=models.UniqueConstraint(fields=('club', 'date', 'time'),
                                               name='session_pk'),
        ),
    ]
