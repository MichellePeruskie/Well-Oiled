# Generated by Django 2.2 on 2020-12-07 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WellOiled_App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='job_title',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]