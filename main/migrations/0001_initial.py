# Generated by Django 3.1.3 on 2020-12-13 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=300)),
                ('price', models.IntegerField(blank=True, default=None, null=True)),
                ('imgsrc', models.ImageField(blank=True, default=None, upload_to='static/images/products')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.category')),
            ],
        ),
    ]