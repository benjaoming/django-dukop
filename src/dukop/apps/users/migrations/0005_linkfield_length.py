# Generated by Django 2.2.17 on 2021-01-11 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_email_verbose_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='link1',
            field=models.URLField(blank=True, max_length=2048, null=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='link2',
            field=models.URLField(blank=True, max_length=2048, null=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='link3',
            field=models.URLField(blank=True, max_length=2048, null=True),
        ),
    ]
