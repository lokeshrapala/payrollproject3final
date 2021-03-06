# Generated by Django 2.0.7 on 2018-12-11 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paymentapp', '0002_company_emp_data_hr_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Finance_Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acid', models.CharField(max_length=7)),
                ('fname', models.CharField(max_length=10)),
                ('lname', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=20)),
                ('mobno', models.CharField(max_length=15)),
                ('add', models.CharField(max_length=50)),
                ('company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='paymentapp.Company')),
            ],
        ),
    ]
