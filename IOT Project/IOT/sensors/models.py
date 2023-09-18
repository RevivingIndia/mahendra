from django.db import models

customertype = (("Individual","Individual"),
                ("Company","Company")
                )

class customer(models.Model):
    customer_id = models.CharField(primary_key=True,max_length=100)
    customer_name = models.CharField(max_length=100)
    customer_type= models.CharField(max_length=100,choices=customertype)
    customer_email = models.EmailField()
    customer_mobile = models.IntegerField()
    customer_address = models.TextField()
    customer_Identity = models.TextField()
    customer_gst = models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return self.customer_name +"--"+self.customer_id

sensorstatus = (
    ("Active","Active"),
    ("InActive","Inactive")
)

class sensor(models.Model):
    sensor_id = models.CharField(primary_key=True,max_length=100)
    sensor_name = models.CharField(max_length=100)
    sensor_status = models.CharField(max_length=20,choices=sensorstatus)
    sensor_value = models.TextField()
    sensor_timestamp = models.DateTimeField()

    def __str__(self):
        return self.sensor_name +"--"+self.sensor_id


class Notification(models.Model):
    customer_id = models.ForeignKey(customer,on_delete=models.CASCADE)
    sensor_id = models.ForeignKey(sensor,on_delete=models.CASCADE)
    notification_id = models.CharField(primary_key=True,max_length=100)
    message = models.TextField()
    flag = models.BooleanField(default=False)

    def __str__(self):
        return self.notification_id