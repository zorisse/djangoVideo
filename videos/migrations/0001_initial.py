# Generated by Django 2.2.4 on 2019-08-30 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date_sortie', models.IntegerField()),
                ('nbr_en_stock', models.IntegerField()),
                ('prix', models.FloatField()),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videos.Genre')),
            ],
        ),
    ]