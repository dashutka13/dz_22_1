# Generated by Django 4.0 on 2024-02-07 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_blog'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ('blog_title',), 'verbose_name': 'публикация', 'verbose_name_plural': 'публикации'},
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='title',
            new_name='blog_title',
        ),
    ]
