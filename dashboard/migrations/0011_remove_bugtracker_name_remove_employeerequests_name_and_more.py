# Generated by Django 4.1.2 on 2022-11-07 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_profile_depart'),
        ('dashboard', '0010_alter_report_issuetype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bugtracker',
            name='name',
        ),
        migrations.RemoveField(
            model_name='employeerequests',
            name='name',
        ),
        migrations.AddField(
            model_name='bugtracker',
            name='issued_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.profile'),
        ),
        migrations.AddField(
            model_name='employeerequests',
            name='requested_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.profile'),
        ),
        migrations.AddField(
            model_name='report',
            name='issued_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.profile'),
        ),
    ]