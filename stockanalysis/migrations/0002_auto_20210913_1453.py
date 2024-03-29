# Generated by Django 3.2.6 on 2021-09-13 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockanalysis', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qualityanalysisscoring',
            name='dividends',
            field=models.CharField(choices=[('0.0', 'No'), ('1.0', 'Yes')], max_length=10),
        ),
        migrations.AlterField(
            model_name='qualityanalysisscoring',
            name='earning_per_share',
            field=models.CharField(choices=[('0.0', 'No'), ('1.0', 'Yes')], max_length=10),
        ),
        migrations.AlterField(
            model_name='qualityanalysisscoring',
            name='free_cash_flow',
            field=models.CharField(choices=[('0.0', 'No'), ('1.0', 'Yes')], max_length=10),
        ),
        migrations.AlterField(
            model_name='qualityanalysisscoring',
            name='government_regulations_risk',
            field=models.CharField(choices=[('0.0', 'No'), ('-1.0', 'Yes')], max_length=10),
        ),
        migrations.AlterField(
            model_name='qualityanalysisscoring',
            name='interest_coverage_ratio',
            field=models.CharField(choices=[('0.0', 'No'), ('0.5', 'greater than 4'), ('1.0', 'greater than 10')], max_length=10),
        ),
        migrations.AlterField(
            model_name='qualityanalysisscoring',
            name='key_person_risk',
            field=models.CharField(choices=[('0.0', 'No'), ('-1.0', 'Yes')], max_length=10),
        ),
        migrations.AlterField(
            model_name='qualityanalysisscoring',
            name='net_profit_margin',
            field=models.CharField(choices=[('-1.0', 'less than 5 percent'), ('-0.5', '5 to 10 percent'), ('1.0', '10 to 15 percent'), ('2.0', '15 to 20 percent'), ('3.0', 'greater than 20 percent')], max_length=10),
        ),
        migrations.AlterField(
            model_name='qualityanalysisscoring',
            name='research_and_development_risk',
            field=models.CharField(choices=[('0.0', 'No'), ('-1.0', 'Yes')], max_length=10),
        ),
        migrations.AlterField(
            model_name='qualityanalysisscoring',
            name='return_on_capital_employed',
            field=models.CharField(choices=[('0.0', 'less than 5 percent'), ('1.0', '5 to 10 percent'), ('2.0', '10 to 15 percent'), ('3.0', '15 to 20 percent'), ('4.0', 'greater than 20 percent')], max_length=10),
        ),
    ]
