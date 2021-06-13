# Generated by Django 3.2.4 on 2021-06-12 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='poll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('option_one', models.CharField(max_length=20)),
                ('option_two', models.CharField(max_length=20)),
                ('option_three', models.CharField(max_length=20)),
                ('option_one_count', models.IntegerField(default=0)),
                ('option_two_count', models.IntegerField(default=0)),
                ('option_three_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='PollApp',
        ),
    ]
