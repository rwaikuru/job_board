# Generated by Django 5.0.4 on 2024-04-24 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_alter_notification_notification_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='resume',
            new_name='cv',
        ),
        migrations.RemoveField(
            model_name='user',
            name='contact_information',
        ),
        migrations.AddField(
            model_name='user',
            name='alternate_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='linkedin_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='physical_address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='po_box',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='postal_address',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='postal_code',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='telephone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
