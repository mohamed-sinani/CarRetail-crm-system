importdjango.db.models.deletion
fromdjango.confimportsettings
fromdjango.dbimportmigrations,models
classMigration(migrations.Migration):
    initial=True
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]
    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id',models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='ID')),
                ('full_name',models.CharField(max_length=140)),
                ('phone',models.CharField(max_length=30)),
                ('email',models.EmailField(blank=True,max_length=254)),
                ('address',models.TextField(blank=True)),
                ('created_at',models.DateTimeField(auto_now_add=True)),
                ('assigned_salesperson',models.ForeignKey(blank=True,limit_choices_to={'role':'SALES'},null=True,on_delete=django.db.models.deletion.SET_NULL,related_name='assigned_customers',to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering':['full_name'],
            },
        ),
    ]
