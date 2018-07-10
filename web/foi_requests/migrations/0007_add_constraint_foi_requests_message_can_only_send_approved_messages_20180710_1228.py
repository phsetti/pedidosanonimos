# Generated by Django 2.0.2 on 2018-07-10 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foi_requests', '0006_auto_20180710_1228'),
    ]

    operations = [
        migrations.RunSQL([
            'ALTER TABLE foi_requests_message ADD CONSTRAINT only_approved_messages_can_have_sent_at CHECK (sent_at IS NULL OR moderation_status IS TRUE);',
        ], [
            'ALTER TABLE foi_requests_message DROP CONSTRAINT only_approved_messages_can_have_sent_at;',
        ])
    ]