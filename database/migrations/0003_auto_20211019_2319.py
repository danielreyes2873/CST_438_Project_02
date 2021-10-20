# Generated by Django 3.2.7 on 2021-10-19 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_remove_items_users'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Users',
        ),
        migrations.AddField(
            model_name='items',
            name='imageUrl',
            field=models.CharField(default='image', max_length=250),
        ),
        migrations.AddField(
            model_name='items',
            name='name',
            field=models.CharField(default='item', max_length=60),
        ),
        migrations.AddField(
            model_name='items',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='items',
            name='priority',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='items',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]