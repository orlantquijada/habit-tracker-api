# Generated by Django 3.0.6 on 2020-06-21 07:49

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0003_auto_20200615_0134'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=30)),
                ('datetime_started', models.DateTimeField(default=django.utils.timezone.now)),
                ('datetime_ended', models.DateTimeField()),
                ('habit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='habits.Habit')),
            ],
            options={
                'verbose_name_plural': 'Entries',
            },
        ),
    ]
