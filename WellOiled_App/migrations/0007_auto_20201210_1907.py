# Generated by Django 2.2 on 2020-12-11 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WellOiled_App', '0006_auto_20201210_1240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='home_office',
        ),
        migrations.AddField(
            model_name='employee',
            name='zipcode',
            field=models.CharField(default=0, max_length=5),
            preserve_default=False,
        ),
    ]
