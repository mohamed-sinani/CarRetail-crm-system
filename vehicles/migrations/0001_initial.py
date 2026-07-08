from django.db import migrations,models
class Migration(migrations.Migration):
    initial=True
    dependencies = [
    ]
    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id',models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='ID')),
                ('brand',models.CharField(max_length=80)),
                ('model',models.CharField(max_length=80)),
                ('year',models.PositiveIntegerField()),
                ('price',models.DecimalField(decimal_places=2,max_digits=12)),
                ('mileage',models.PositiveIntegerField()),
                ('transmission',models.CharField(choices=[('AUTOMATIC','Automatic'),('MANUAL','Manual'),('CVT','CVT')],max_length=20)),
                ('fuel_type',models.CharField(choices=[('PETROL','Petrol'),('DIESEL','Diesel'),('HYBRID','Hybrid'),('ELECTRIC','Electric')],max_length=20)),
                ('status',models.CharField(choices=[('AVAILABLE','Available'),('RESERVED','Reserved'),('SOLD','Sold')],default='AVAILABLE',max_length=20)),
                ('image',models.FileField(blank=True,null=True,upload_to='vehicles/')),
                ('created_at',models.DateTimeField(auto_now_add=True)),
                ('updated_at',models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering':['brand','model','-year'],
            },
        ),
    ]
