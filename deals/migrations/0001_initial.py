importdjango.db.models.deletion
from django.conf import settings
from django.db import migrations,models
class Migration(migrations.Migration):
    initial=True
    dependencies = [
        ('customers','0001_initial'),
        ('vehicles','0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]
    operations = [
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id',models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='ID')),
                ('stage',models.CharField(choices=[('NEW_LEAD','New Lead'),('CONTACTED','Contacted'),('NEGOTIATION','Negotiation'),('PAYMENT_PENDING','Payment Pending'),('CLOSED_WON','Closed Won'),('CLOSED_LOST','Closed Lost')],default='NEW_LEAD',max_length=30)),
                ('expected_value',models.DecimalField(decimal_places=2,default=0,max_digits=12)),
                ('notes',models.TextField(blank=True)),
                ('created_at',models.DateTimeField(auto_now_add=True)),
                ('updated_at',models.DateTimeField(auto_now=True)),
                ('customer',models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,related_name='deals',to='customers.customer')),
                ('salesperson',models.ForeignKey(null=True,on_delete=django.db.models.deletion.SET_NULL,related_name='deals',to=settings.AUTH_USER_MODEL)),
                ('vehicle',models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,related_name='deals',to='vehicles.vehicle')),
            ],
            options={
                'ordering':['stage','-updated_at'],
            },
        ),
    ]
