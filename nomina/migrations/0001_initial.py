# Generated by Django 2.2.7 on 2019-12-05 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Impuesto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('short_name', models.CharField(max_length=8)),
                ('liable', models.CharField(choices=[('EMPLOYEE', 'EMPLOYEE'), ('COMPANY', 'COMPANY')], default='COMPANY', max_length=10)),
                ('tax_rate', models.DecimalField(decimal_places=8, max_digits=10)),
                ('due_date', models.IntegerField()),
            ],
        ),
    ]
