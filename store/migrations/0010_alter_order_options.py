# Generated by Django 4.1.5 on 2023-03-20 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_alter_customer_options_remove_customer_email_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'permissions': [('cancel_order', 'Can Cancel order')]},
        ),
    ]
