# Generated by Django 4.2 on 2023-04-22 21:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crimsonboard', '0015_alter_assignmentresponse_assignment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignments',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='course_assignments', to='crimsonboard.course'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='assignments',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='assignments',
            name='instructor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='crimsonboard.instructor'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='assignments',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
