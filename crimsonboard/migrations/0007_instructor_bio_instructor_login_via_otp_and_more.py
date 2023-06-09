# Generated by Django 4.2 on 2023-04-20 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crimsonboard', '0006_student_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='bio',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='instructor',
            name='login_via_otp',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='instructor',
            name='otp_digit',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='instructor',
            name='profile_image',
            field=models.ImageField(null=True, upload_to='instructor_profile_imgs/'),
        ),
        migrations.AddField(
            model_name='instructor',
            name='verify_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='student',
            name='login_via_otp',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='student',
            name='otp_digit',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='verify_status',
            field=models.BooleanField(default=False),
        ),
    ]
