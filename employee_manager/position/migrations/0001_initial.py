# Generated by Django 5.0.4 on 2024-05-12 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='position',
            fields=[
                ('position_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
