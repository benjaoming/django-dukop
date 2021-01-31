# Generated by Django 2.2.17 on 2021-01-11 23:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calendar', '0010_intervals'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='host',
            field=models.ForeignKey(blank=True, help_text='A group may host an event and be displayed as the author of the event text.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='events', to='users.Group'),
        ),
        migrations.AlterField(
            model_name='eventlink',
            name='link',
            field=models.URLField(blank=True, max_length=2048, null=True),
        ),
    ]