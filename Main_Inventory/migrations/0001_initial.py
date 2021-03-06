# Generated by Django 3.0.3 on 2020-03-08 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('empusername', models.TextField()),
                ('soldto', models.TextField()),
                ('profit', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productid', models.TextField()),
                ('sellingprice', models.TextField()),
                ('quantity', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='emp_det',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('username', models.TextField()),
                ('mobile', models.TextField()),
                ('address', models.TextField()),
                ('email', models.TextField()),
                ('gender', models.TextField()),
                ('dob', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('cost', models.TextField()),
                ('quantity', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='sold_products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productid', models.TextField()),
                ('billid', models.TextField()),
                ('sellingprice', models.TextField()),
                ('quantity', models.TextField()),
            ],
        ),
    ]
