# Generated by Django 4.1 on 2022-08-30 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_alter_subtask_head_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='is_published',
        ),
        migrations.RemoveField(
            model_name='task',
            name='status',
        ),
        migrations.AddField(
            model_name='task',
            name='color',
            field=models.CharField(default='white', max_length=20),
            preserve_default=False,
        ),
    ]
