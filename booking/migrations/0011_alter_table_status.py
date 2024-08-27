# Generated by Django 4.2.15 on 2024-08-27 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0010_alter_table_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='status',
            field=models.IntegerField(choices=[('1', 'Available'), ('2', 'Reserved'), ('0', 'Cancelled')], default=1, max_length=10),
        ),
    ]
