# Generated by Django 3.1.7 on 2021-04-21 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automobile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=150)),
                ('modelo_marca', models.CharField(max_length=150)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('delete_at', models.DateTimeField()),
            ],
        ),
    ]