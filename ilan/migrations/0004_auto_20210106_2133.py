# Generated by Django 3.1.4 on 2021-01-06 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ilan', '0003_auto_20210106_0431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ilan',
            name='ilan_image',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Görsel Ekle'),
        ),
    ]
