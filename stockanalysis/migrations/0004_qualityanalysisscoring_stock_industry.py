# Generated by Django 3.2.6 on 2021-12-18 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockanalysis', '0003_stocktrendsignals'),
    ]

    operations = [
        migrations.AddField(
            model_name='qualityanalysisscoring',
            name='stock_industry',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Stock Industry'),
        ),
    ]
