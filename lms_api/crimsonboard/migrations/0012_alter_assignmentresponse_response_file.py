# Generated by Django 4.2 on 2023-04-21 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crimsonboard', '0011_assignments_assignmentresponse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignmentresponse',
            name='response_file',
            field=models.FileField(null=True, upload_to='responses/'),
        ),
    ]