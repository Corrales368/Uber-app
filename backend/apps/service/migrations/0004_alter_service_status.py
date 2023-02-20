# Generated by Django 4.1.7 on 2023-02-20 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_alter_service_distance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='status',
            field=models.IntegerField(choices=[(0, 'Unassigned'), (1, 'Assigned'), (2, 'Completed'), (3, 'Canceled')]),
        ),
    ]