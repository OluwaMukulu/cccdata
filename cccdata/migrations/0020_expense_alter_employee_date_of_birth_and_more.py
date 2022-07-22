# Generated by Django 4.0.5 on 2022-06-26 21:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cccdata', '0019_alter_expenses_expense_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('department', models.CharField(choices=[('Mn', 'Management'), ('FD', 'Food/Kitchen'), ('TP', 'Transportion'), ('LG', 'Logistics/Operations'), ('MK', 'Marketing'), ('SV', 'Customer Service'), ('FN', 'Finance')], max_length=2, null=True)),
                ('date', models.DateField(null=True)),
                ('expense_type', models.CharField(choices=[('EO', 'Extra Over'), ('AC', 'Accomodation'), ('CA', 'Communication/Airtime'), ('KT', 'Kitchen'), ('BD', 'Budget'), ('ME', 'Materials and Equipment'), ('FI', 'Food Items'), ('DM', 'Damages'), ('VM', 'Vehicle repair and Maintenance'), ('GS', 'Gas'), ('LB', 'Labor'), ('TX', 'Tax'), ('UN', 'Uniform')], max_length=2)),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=12)),
                ('payment_method', models.CharField(choices=[('CS', 'Cash'), ('CR', 'Card'), ('CD', 'Credit'), ('AM', 'Airtel Money'), ('MM', 'MTN Money'), ('OT', 'Other')], max_length=2)),
                ('activity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cccdata.activity')),
            ],
            options={
                'verbose_name_plural': 'Expenses',
            },
        ),
        migrations.AlterField(
            model_name='employee',
            name='date_of_birth',
            field=models.DateField(blank=True, default='YYYY-MM-DD', null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='actual',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
        migrations.AlterField(
            model_name='event',
            name='budget',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
        migrations.AlterField(
            model_name='event',
            name='contract_sum',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
        migrations.AlterField(
            model_name='ingredients',
            name='profit_per_serving',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='ingredients',
            name='unit_price',
            field=models.DecimalField(decimal_places=2, default='null', max_digits=12),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='inventory',
            name='quantity',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='unit_price',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
        migrations.AlterField(
            model_name='partner',
            name='phone',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='peformance',
            name='salary',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='phone',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
        migrations.DeleteModel(
            name='Expenses',
        ),
        migrations.AddField(
            model_name='expense',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cccdata.event'),
        ),
        migrations.AddField(
            model_name='expense',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cccdata.supplier'),
        ),
    ]
