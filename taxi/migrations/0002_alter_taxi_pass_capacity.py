# Generated by Django 4.2.17 on 2024-12-05 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taxi',
            name='pass_capacity',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
