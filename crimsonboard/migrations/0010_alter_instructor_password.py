# Generated by Django 4.2 on 2023-04-20 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crimsonboard', '0009_instructor_bio_instructor_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='password',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
