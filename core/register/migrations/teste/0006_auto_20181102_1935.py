# Generated by Django 2.1.3 on 2018-11-02 22:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0005_remove_phones_cli'),
    ]

    operations = [
        migrations.AddField(
            model_name='phones',
            name='cli',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='RegCli', to='register.RegCli'),
        ),
        migrations.AlterField(
            model_name='regcli',
            name='com_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
