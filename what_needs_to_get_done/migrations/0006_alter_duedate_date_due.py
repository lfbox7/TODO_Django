# Generated by Django 3.2 on 2021-04-27 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('what_needs_to_get_done', '0005_alter_status_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duedate',
            name='date_due',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]