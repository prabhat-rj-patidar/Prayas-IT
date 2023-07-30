# Generated by Django 4.2 on 2023-05-17 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_recruiterreg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('salary', models.FloatField(max_length=10)),
                ('image', models.CharField(max_length=10)),
                ('company', models.FileField(upload_to='')),
                ('location', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=300)),
                ('creationdate', models.DateField()),
                ('recruiter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.recruiterreg')),
            ],
        ),
    ]