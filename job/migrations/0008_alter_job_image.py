# Generated by Django 4.2 on 2023-05-17 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0007_alter_job_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='image',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
