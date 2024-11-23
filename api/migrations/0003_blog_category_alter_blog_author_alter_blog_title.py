# Generated by Django 5.1.2 on 2024-11-23 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_circular'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.CharField(choices=[('job', 'Job'), ('admission', 'Admission')], default='job', max_length=10),
        ),
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]