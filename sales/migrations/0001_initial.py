importdjango.db.models.deletion
fromdjango.confimportsettings
fromdjango.dbimportmigrations,models
classMigration(migrations.Migration):
    initial=True
    dependencies = [
        ('customers','0001_initial'),
        ('vehicles','0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]
    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id',models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='ID')),
                ('amount',models.DecimalField(decimal_places=2,max_digits=12)),
                ('payment_method',models.CharField(choices=[('CASH','Cash'),('BANK_TRANSFER','Bank Transfer'),('FINANCE','Finance'),('CARD','Card')],max_length=30)),
                ('sale_date',models.DateField()),
                ('created_at',models.DateTimeField(auto_now_add=True)),
                ('customer',models.ForeignKey(on_delete=django.db.models.deletion.PROTECT,related_name='sales',to='customers.customer')),
                ('salesperson',models.ForeignKey(null=True,on_delete=django.db.models.deletion.SET_NULL,related_name='sales',to=settings.AUTH_USER_MODEL)),
                ('vehicle',models.OneToOneField(on_delete=django.db.models.deletion.PROTECT,related_name='sale',to='vehicles.vehicle')),
            ],
            options={
                'ordering':['-sale_date','-created_at'],
            },
        ),
    ]
