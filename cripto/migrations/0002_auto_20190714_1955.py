# Generated by Django 2.2.3 on 2019-07-14 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cripto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='self',
            name='df_key',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
