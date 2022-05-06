# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Ams(models.Model):
    id = models.BigIntegerField(primary_key=True)
    avg_mon_sales_for_a_year = models.CharField(max_length=50, blank=True, null=True)
    datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ams'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cu(models.Model):
    customer_code = models.CharField(primary_key=True, max_length=50)
    group_name = models.CharField(max_length=50, blank=True, null=True)
    performance_this_month = models.CharField(max_length=50, blank=True, null=True)
    datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cu'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DjangoTraceAudit(models.Model):
    date = models.DateTimeField()
    action = models.PositiveIntegerField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_trace_audit'


class DjangoTraceLog(models.Model):
    method = models.CharField(max_length=10)
    path = models.TextField()
    host = models.CharField(max_length=300)
    session = models.CharField(max_length=300, blank=True, null=True)
    start = models.DateTimeField()
    info = models.TextField(blank=True, null=True)
    duration = models.FloatField()
    status = models.PositiveIntegerField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_trace_log'


class Gp(models.Model):
    group_name = models.CharField(primary_key=True, max_length=50)
    dept = models.CharField(max_length=50, blank=True, null=True)
    responsible_person = models.CharField(max_length=50, blank=True, null=True)
    target = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gp'


class Inv(models.Model):
    id = models.BigIntegerField(primary_key=True)
    product_id = models.IntegerField(blank=True, null=True)
    product_name = models.CharField(max_length=50, blank=True, null=True)
    packing = models.CharField(max_length=50, blank=True, null=True)
    inv_qty = models.IntegerField(blank=True, null=True)
    packing_qty = models.CharField(max_length=50, blank=True, null=True)
    exp = models.CharField(max_length=50, blank=True, null=True)
    avg_mthly_sales = models.IntegerField(blank=True, null=True)
    avg_daily_sales = models.IntegerField(blank=True, null=True)
    days_sold_out = models.IntegerField(blank=True, null=True)
    days_of_arrival = models.IntegerField(blank=True, null=True)
    rep_notice = models.CharField(max_length=50, blank=True, null=True)
    mfd = models.CharField(max_length=50, blank=True, null=True)
    days_after_manu = models.IntegerField(blank=True, null=True)
    six_mos_warning = models.CharField(max_length=50, blank=True, null=True)
    three_mos_warning = models.CharField(max_length=50, blank=True, null=True)
    seq = models.IntegerField(blank=True, null=True)
    datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'inv'


class Inv01002(models.Model):
    product_id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=50, blank=True, null=True)
    spec = models.CharField(max_length=50, blank=True, null=True)
    factory_code = models.CharField(max_length=50, blank=True, null=True)
    factory_name = models.CharField(max_length=50, blank=True, null=True)
    inv_qty = models.CharField(max_length=50, blank=True, null=True)
    unit = models.CharField(max_length=50, blank=True, null=True)
    small_unit = models.CharField(max_length=50, blank=True, null=True)
    storage_spaces = models.CharField(max_length=50, blank=True, null=True)
    quantity_at_the_beginning_of_the_month = models.CharField(max_length=50, blank=True, null=True)
    the_most_recent_storage_date = models.CharField(max_length=50, blank=True, null=True)
    the_most_recent_out_of_the_warehouse_day = models.CharField(max_length=50, blank=True, null=True)
    last_count_date = models.CharField(max_length=50, blank=True, null=True)
    safety_stock = models.CharField(max_length=50, blank=True, null=True)
    replenishment_point = models.CharField(max_length=50, blank=True, null=True)
    economic_batch = models.CharField(max_length=50, blank=True, null=True)
    standard_inventory = models.CharField(max_length=50, blank=True, null=True)
    standard_turnover_rate = models.CharField(max_length=50, blank=True, null=True)
    inventory_packaging_quantity = models.CharField(max_length=50, blank=True, null=True)
    package_quantity_at_the_beginning_of_the_month = models.CharField(max_length=50, blank=True, null=True)
    datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'inv01002'


class Line(models.Model):
    line_id = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=50, blank=True, null=True)
    permission_name = models.CharField(max_length=50, blank=True, null=True)
    datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'line'


class LinePermission(models.Model):
    permission_name = models.CharField(primary_key=True, max_length=255)
    order = models.CharField(max_length=50, blank=True, null=True)
    dsv_inv = models.CharField(max_length=50, blank=True, null=True)
    finished_product_inv = models.CharField(max_length=50, blank=True, null=True)
    pp = models.CharField(max_length=50, blank=True, null=True)
    prom = models.CharField(max_length=50, blank=True, null=True)
    datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'line_permission'


class Mssq(models.Model):
    id = models.BigIntegerField(primary_key=True)
    store_code = models.CharField(max_length=50, blank=True, null=True)
    product_id = models.BigIntegerField()
    product_name = models.CharField(max_length=50, blank=True, null=True)
    year = models.CharField(max_length=50, blank=True, null=True)
    january = models.CharField(max_length=50, blank=True, null=True)
    february = models.CharField(max_length=50, blank=True, null=True)
    march = models.CharField(max_length=50, blank=True, null=True)
    april = models.CharField(max_length=50, blank=True, null=True)
    may = models.CharField(max_length=50, blank=True, null=True)
    june = models.CharField(max_length=50, blank=True, null=True)
    july = models.CharField(max_length=50, blank=True, null=True)
    august = models.CharField(max_length=50, blank=True, null=True)
    september = models.CharField(max_length=50, blank=True, null=True)
    october = models.CharField(max_length=50, blank=True, null=True)
    november = models.CharField(max_length=50, blank=True, null=True)
    december = models.CharField(max_length=50, blank=True, null=True)
    datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'mssq'


class Pp(models.Model):
    id = models.BigIntegerField(primary_key=True)
    international_barcode = models.CharField(max_length=50, blank=True, null=True)
    product_name = models.CharField(max_length=50)
    spec = models.CharField(max_length=50, blank=True, null=True)
    broken_number = models.CharField(max_length=50, blank=True, null=True)
    suggested_price = models.CharField(max_length=50, blank=True, null=True)
    purchase_price = models.CharField(max_length=50, blank=True, null=True)
    tax = models.CharField(max_length=50, blank=True, null=True)
    normal_gift = models.CharField(max_length=50, blank=True, null=True)
    average_price = models.CharField(max_length=50, blank=True, null=True)
    first_stage = models.CharField(max_length=50, blank=True, null=True)
    second_stage = models.CharField(max_length=50, blank=True, null=True)
    first_stage_average_price = models.CharField(max_length=50, blank=True, null=True)
    second_stage_average_price = models.CharField(max_length=50, blank=True, null=True)
    gp_after_new_avg_price_of_5_boxes = models.CharField(max_length=50, blank=True, null=True)
    old_declared_purchase_price = models.CharField(max_length=50, blank=True, null=True)
    old_way_to_declare_discounts = models.CharField(max_length=50, blank=True, null=True)
    avg_price_of_old_declaration = models.CharField(max_length=50, blank=True, null=True)
    more_than_five_boxes = models.CharField(max_length=50, blank=True, null=True)
    datetime = models.DateTimeField()
    expected_price_increase_date = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pp'
        unique_together = (('id', 'product_name'),)


class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=50)
    origin = models.CharField(max_length=50, blank=True, null=True)
    ingredients = models.CharField(db_column='Ingredients', max_length=50, blank=True, null=True)  # Field name made lowercase.
    specification = models.CharField(max_length=50, blank=True, null=True)
    product_pic = models.TextField(blank=True, null=True)
    original_price = models.IntegerField(blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product'
        unique_together = (('product_id', 'product_name'),)


class Prom(models.Model):
    id = models.BigIntegerField(primary_key=True)
    product_name = models.CharField(max_length=50)
    special_offer = models.CharField(max_length=50, blank=True, null=True)
    special_purchase_price = models.CharField(max_length=50, blank=True, null=True)
    note = models.CharField(max_length=50, blank=True, null=True)
    datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'prom'
        unique_together = (('id', 'product_name'),)


class Sq(models.Model):
    id = models.BigIntegerField()
    product_name = models.CharField(max_length=50, blank=True, null=True)
    customer_code = models.CharField(max_length=50, blank=True, null=True)
    sale_date = models.CharField(max_length=50, blank=True, null=True)
    sales_number = models.CharField(primary_key=True, max_length=50)
    sales_quantity = models.CharField(max_length=50, blank=True, null=True)
    sales_packaging_quantity = models.CharField(max_length=50, blank=True, null=True)
    units = models.CharField(max_length=50, blank=True, null=True)
    currencies = models.CharField(max_length=50, blank=True, null=True)
    unit_price = models.CharField(max_length=50, blank=True, null=True)
    original_currency_untaxed_amount = models.CharField(max_length=50, blank=True, null=True)
    untaxed_amount_in_local_currency = models.CharField(max_length=50, blank=True, null=True)
    cost_of_goods_sold = models.CharField(max_length=50, blank=True, null=True)
    gross_profit_margin = models.CharField(max_length=50, blank=True, null=True)
    invoice_coupon = models.CharField(max_length=50, blank=True, null=True)
    salesman = models.CharField(max_length=50, blank=True, null=True)
    factory_code = models.CharField(max_length=50, blank=True, null=True)
    library_code = models.CharField(max_length=50, blank=True, null=True)
    group_name = models.CharField(max_length=50, blank=True, null=True)
    year_sq_sum = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sq'


class Ssq(models.Model):
    id = models.BigIntegerField(primary_key=True)
    year = models.CharField(max_length=50, blank=True, null=True)
    month = models.CharField(max_length=50, blank=True, null=True)
    product_id = models.BigIntegerField()
    store_code = models.CharField(max_length=50, blank=True, null=True)
    product_name = models.CharField(max_length=50, blank=True, null=True)
    spec = models.CharField(max_length=50, blank=True, null=True)
    sales_quantity = models.CharField(max_length=50, blank=True, null=True)
    total_sales = models.CharField(max_length=50, blank=True, null=True)
    total_sales_before_tax = models.CharField(max_length=50, blank=True, null=True)
    average_unit_price = models.CharField(max_length=50, blank=True, null=True)
    net_sales = models.CharField(max_length=50, blank=True, null=True)
    total_amount_of_discount = models.CharField(max_length=50, blank=True, null=True)
    number_of_giveaways = models.CharField(max_length=50, blank=True, null=True)
    weight = models.CharField(max_length=50, blank=True, null=True)
    giveaway_weight = models.CharField(max_length=50, blank=True, null=True)
    cost_of_goods_sold = models.CharField(max_length=50, blank=True, null=True)
    gross_sales = models.CharField(max_length=50, blank=True, null=True)
    gross_profit_margin = models.CharField(max_length=50, blank=True, null=True)
    datetime = models.DateTimeField()
    year_ssq_sum = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ssq'
