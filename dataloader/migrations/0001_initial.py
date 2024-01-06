# Generated by Django 3.2.6 on 2021-08-15 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BhavcopyRaw',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bhavcopy_csv_file', models.FileField(upload_to='./data/bhavcopy/uploads/')),
                ('file_date', models.DateField()),
                ('upload_date', models.DateField(auto_now_add=True)),
                ('processing_date', models.DateTimeField(auto_now=True, null=True)),
                ('file_status', models.CharField(choices=[('Uploaded', 'Uploaded'), ('Uploading Failed', 'Uploading Failed'), ('Under Process', 'Under Process'), ('Processing Completed', 'Processing Completed'), ('Processing Failed', 'Processing Failed')], default='File Status', max_length=200)),
            ],
        ),
    ]
