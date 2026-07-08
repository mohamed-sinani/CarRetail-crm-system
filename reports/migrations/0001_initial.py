fromdjango.dbimportmigrations,models
classMigration(migrations.Migration):
    initial=True
    dependencies = [
    ]
    operations = [
        migrations.CreateModel(
            name='ReportSnapshot',
            fields=[
                ('id',models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='ID')),
                ('report_type',models.CharField(choices=[('SALES','Sales'),('INVENTORY','Inventory'),('REVENUE','Revenue')],max_length=20)),
                ('title',models.CharField(max_length=160)),
                ('generated_at',models.DateTimeField(auto_now_add=True)),
                ('payload',models.JSONField(blank=True,default=dict)),
            ],
            options={
                'ordering':['-generated_at'],
            },
        ),
    ]
