# Generated by Django 5.1 on 2024-11-27 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_tag_order_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='tag',
        ),
        migrations.AddField(
            model_name='product',
            name='tag',
            field=models.ManyToManyField(to='account.tag'),
        ),
    ]