# Generated by Django 4.2 on 2023-04-22 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crimsonboard', '0014_alter_assignmentresponse_reponse_text_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignmentresponse',
            name='assignment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crimsonboard.assignments'),
        ),
        migrations.AlterField(
            model_name='assignmentresponse',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crimsonboard.course'),
        ),
        migrations.AlterField(
            model_name='assignmentresponse',
            name='reponse_text',
            field=models.TextField(blank=True, default='Submission Done', null=True),
        ),
        migrations.AlterField(
            model_name='assignmentresponse',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crimsonboard.student'),
        ),
        migrations.AlterField(
            model_name='assignmentresponse',
            name='submission_file',
            field=models.FileField(blank=True, null=True, upload_to='responses/'),
        ),
        migrations.AlterField(
            model_name='assignments',
            name='assignment_file',
            field=models.FileField(blank=True, null=True, upload_to='assignments/'),
        ),
        migrations.AlterField(
            model_name='assignments',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course_assignments', to='crimsonboard.course'),
        ),
        migrations.AlterField(
            model_name='assignments',
            name='deadline',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='assignments',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='assignments',
            name='instructor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crimsonboard.instructor'),
        ),
        migrations.AlterField(
            model_name='assignments',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
