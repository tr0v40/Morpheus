# Generated by Django 2.1.3 on 2018-11-02 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prod',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('product', models.CharField(max_length=100)),
                ('ncm', models.CharField(max_length=100)),
            ],
        ),
    ]
