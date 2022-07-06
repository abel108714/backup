# Generated by Django 3.1.11 on 2022-05-03 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ams',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('avg_mon_sales_for_a_year', models.CharField(blank=True, max_length=50, null=True)),
                ('datetime', models.DateTimeField()),
            ],
            options={
                'db_table': 'ams',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cu',
            fields=[
                ('customer_code', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('group_name', models.CharField(blank=True, max_length=50, null=True)),
                ('performance_this_month', models.CharField(blank=True, max_length=50, null=True)),
                ('datetime', models.DateTimeField()),
            ],
            options={
                'db_table': 'cu',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Gp',
            fields=[
                ('group_name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('dept', models.CharField(blank=True, max_length=50, null=True)),
                ('responsible_person', models.CharField(blank=True, max_length=50, null=True)),
                ('target', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'gp',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Inv',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('product_id', models.IntegerField(blank=True, null=True)),
                ('product_name', models.CharField(blank=True, max_length=50, null=True)),
                ('packing', models.CharField(blank=True, max_length=50, null=True)),
                ('inv_qty', models.IntegerField(blank=True, null=True)),
                ('packing_qty', models.CharField(blank=True, max_length=50, null=True)),
                ('exp', models.CharField(blank=True, max_length=50, null=True)),
                ('avg_mthly_sales', models.IntegerField(blank=True, null=True)),
                ('avg_daily_sales', models.IntegerField(blank=True, null=True)),
                ('days_sold_out', models.IntegerField(blank=True, null=True)),
                ('days_of_arrival', models.IntegerField(blank=True, null=True)),
                ('rep_notice', models.CharField(blank=True, max_length=50, null=True)),
                ('mfd', models.CharField(blank=True, max_length=50, null=True)),
                ('days_after_manu', models.IntegerField(blank=True, null=True)),
                ('six_mos_warning', models.CharField(blank=True, max_length=50, null=True)),
                ('three_mos_warning', models.CharField(blank=True, max_length=50, null=True)),
                ('seq', models.IntegerField(blank=True, null=True)),
                ('datetime', models.DateTimeField()),
            ],
            options={
                'db_table': 'inv',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Inv01002',
            fields=[
                ('product_id', models.IntegerField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(blank=True, max_length=50, null=True)),
                ('spec', models.CharField(blank=True, max_length=50, null=True)),
                ('factory_code', models.CharField(blank=True, max_length=50, null=True)),
                ('factory_name', models.CharField(blank=True, max_length=50, null=True)),
                ('inv_qty', models.CharField(blank=True, max_length=50, null=True)),
                ('unit', models.CharField(blank=True, max_length=50, null=True)),
                ('small_unit', models.CharField(blank=True, max_length=50, null=True)),
                ('storage_spaces', models.CharField(blank=True, max_length=50, null=True)),
                ('quantity_at_the_beginning_of_the_month', models.CharField(blank=True, max_length=50, null=True)),
                ('the_most_recent_storage_date', models.CharField(blank=True, max_length=50, null=True)),
                ('the_most_recent_out_of_the_warehouse_day', models.CharField(blank=True, max_length=50, null=True)),
                ('last_count_date', models.CharField(blank=True, max_length=50, null=True)),
                ('safety_stock', models.CharField(blank=True, max_length=50, null=True)),
                ('replenishment_point', models.CharField(blank=True, max_length=50, null=True)),
                ('economic_batch', models.CharField(blank=True, max_length=50, null=True)),
                ('standard_inventory', models.CharField(blank=True, max_length=50, null=True)),
                ('standard_turnover_rate', models.CharField(blank=True, max_length=50, null=True)),
                ('inventory_packaging_quantity', models.CharField(blank=True, max_length=50, null=True)),
                ('package_quantity_at_the_beginning_of_the_month', models.CharField(blank=True, max_length=50, null=True)),
                ('datetime', models.DateTimeField()),
            ],
            options={
                'db_table': 'inv01002',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Line',
            fields=[
                ('line_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('permission_name', models.CharField(blank=True, max_length=50, null=True)),
                ('datetime', models.DateTimeField()),
            ],
            options={
                'db_table': 'line',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LinePermission',
            fields=[
                ('permission_name', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('order', models.CharField(blank=True, max_length=50, null=True)),
                ('dsv_inv', models.CharField(blank=True, max_length=50, null=True)),
                ('finished_product_inv', models.CharField(blank=True, max_length=50, null=True)),
                ('pp', models.CharField(blank=True, max_length=50, null=True)),
                ('prom', models.CharField(blank=True, max_length=50, null=True)),
                ('datetime', models.DateTimeField()),
            ],
            options={
                'db_table': 'line_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Mssq',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('store_code', models.CharField(blank=True, max_length=50, null=True)),
                ('product_id', models.BigIntegerField()),
                ('product_name', models.CharField(blank=True, max_length=50, null=True)),
                ('year', models.CharField(blank=True, max_length=50, null=True)),
                ('january', models.CharField(blank=True, max_length=50, null=True)),
                ('february', models.CharField(blank=True, max_length=50, null=True)),
                ('march', models.CharField(blank=True, max_length=50, null=True)),
                ('april', models.CharField(blank=True, max_length=50, null=True)),
                ('may', models.CharField(blank=True, max_length=50, null=True)),
                ('june', models.CharField(blank=True, max_length=50, null=True)),
                ('july', models.CharField(blank=True, max_length=50, null=True)),
                ('august', models.CharField(blank=True, max_length=50, null=True)),
                ('september', models.CharField(blank=True, max_length=50, null=True)),
                ('october', models.CharField(blank=True, max_length=50, null=True)),
                ('november', models.CharField(blank=True, max_length=50, null=True)),
                ('december', models.CharField(blank=True, max_length=50, null=True)),
                ('datetime', models.DateTimeField()),
            ],
            options={
                'db_table': 'mssq',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pp',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('international_barcode', models.CharField(blank=True, max_length=50, null=True)),
                ('product_name', models.CharField(max_length=50)),
                ('spec', models.CharField(blank=True, max_length=50, null=True)),
                ('broken_number', models.CharField(blank=True, max_length=50, null=True)),
                ('suggested_price', models.CharField(blank=True, max_length=50, null=True)),
                ('purchase_price', models.CharField(blank=True, max_length=50, null=True)),
                ('tax', models.CharField(blank=True, max_length=50, null=True)),
                ('normal_gift', models.CharField(blank=True, max_length=50, null=True)),
                ('average_price', models.CharField(blank=True, max_length=50, null=True)),
                ('first_stage', models.CharField(blank=True, max_length=50, null=True)),
                ('second_stage', models.CharField(blank=True, max_length=50, null=True)),
                ('first_stage_average_price', models.CharField(blank=True, max_length=50, null=True)),
                ('second_stage_average_price', models.CharField(blank=True, max_length=50, null=True)),
                ('gp_after_new_avg_price_of_5_boxes', models.CharField(blank=True, max_length=50, null=True)),
                ('old_declared_purchase_price', models.CharField(blank=True, max_length=50, null=True)),
                ('old_way_to_declare_discounts', models.CharField(blank=True, max_length=50, null=True)),
                ('avg_price_of_old_declaration', models.CharField(blank=True, max_length=50, null=True)),
                ('more_than_five_boxes', models.CharField(blank=True, max_length=50, null=True)),
                ('datetime', models.DateTimeField()),
                ('expected_price_increase_date', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'pp',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.IntegerField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=50)),
                ('origin', models.CharField(blank=True, max_length=50, null=True)),
                ('ingredients', models.CharField(blank=True, db_column='Ingredients', max_length=50, null=True)),
                ('specification', models.CharField(blank=True, max_length=50, null=True)),
                ('product_pic', models.TextField(blank=True, null=True)),
                ('original_price', models.IntegerField(blank=True, null=True)),
                ('website', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'product',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Prom',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=50)),
                ('special_offer', models.CharField(blank=True, max_length=50, null=True)),
                ('special_purchase_price', models.CharField(blank=True, max_length=50, null=True)),
                ('note', models.CharField(blank=True, max_length=50, null=True)),
                ('datetime', models.DateTimeField()),
            ],
            options={
                'db_table': 'prom',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sq',
            fields=[
                ('id', models.BigIntegerField()),
                ('product_name', models.CharField(blank=True, max_length=50, null=True)),
                ('customer_code', models.CharField(blank=True, max_length=50, null=True)),
                ('sale_date', models.CharField(blank=True, max_length=50, null=True)),
                ('sales_number', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('sales_quantity', models.CharField(blank=True, max_length=50, null=True)),
                ('sales_packaging_quantity', models.CharField(blank=True, max_length=50, null=True)),
                ('units', models.CharField(blank=True, max_length=50, null=True)),
                ('currencies', models.CharField(blank=True, max_length=50, null=True)),
                ('unit_price', models.CharField(blank=True, max_length=50, null=True)),
                ('original_currency_untaxed_amount', models.CharField(blank=True, max_length=50, null=True)),
                ('untaxed_amount_in_local_currency', models.CharField(blank=True, max_length=50, null=True)),
                ('cost_of_goods_sold', models.CharField(blank=True, max_length=50, null=True)),
                ('gross_profit_margin', models.CharField(blank=True, max_length=50, null=True)),
                ('invoice_coupon', models.CharField(blank=True, max_length=50, null=True)),
                ('salesman', models.CharField(blank=True, max_length=50, null=True)),
                ('factory_code', models.CharField(blank=True, max_length=50, null=True)),
                ('library_code', models.CharField(blank=True, max_length=50, null=True)),
                ('group_name', models.CharField(blank=True, max_length=50, null=True)),
                ('year_sq_sum', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'sq',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ssq',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('year', models.CharField(blank=True, max_length=50, null=True)),
                ('month', models.CharField(blank=True, max_length=50, null=True)),
                ('product_id', models.BigIntegerField()),
                ('store_code', models.CharField(blank=True, max_length=50, null=True)),
                ('product_name', models.CharField(blank=True, max_length=50, null=True)),
                ('spec', models.CharField(blank=True, max_length=50, null=True)),
                ('sales_quantity', models.CharField(blank=True, max_length=50, null=True)),
                ('total_sales', models.CharField(blank=True, max_length=50, null=True)),
                ('total_sales_before_tax', models.CharField(blank=True, max_length=50, null=True)),
                ('average_unit_price', models.CharField(blank=True, max_length=50, null=True)),
                ('net_sales', models.CharField(blank=True, max_length=50, null=True)),
                ('total_amount_of_discount', models.CharField(blank=True, max_length=50, null=True)),
                ('number_of_giveaways', models.CharField(blank=True, max_length=50, null=True)),
                ('weight', models.CharField(blank=True, max_length=50, null=True)),
                ('giveaway_weight', models.CharField(blank=True, max_length=50, null=True)),
                ('cost_of_goods_sold', models.CharField(blank=True, max_length=50, null=True)),
                ('gross_sales', models.CharField(blank=True, max_length=50, null=True)),
                ('gross_profit_margin', models.CharField(blank=True, max_length=50, null=True)),
                ('datetime', models.DateTimeField()),
                ('year_ssq_sum', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'ssq',
                'managed': False,
            },
        ),
    ]
