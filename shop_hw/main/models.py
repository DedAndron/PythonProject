from django.db import models

# Create your models here.

class Buyer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

class Seller(models.Model):
    JOB_TITLE_CHOICES = [
        ('salesperson', 'Salesperson'),
        ('head salesperson', 'Head salesperson'),
        ('sales department manager', 'Sales department manager'),
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    date_of_employment = models.DateField(auto_now_add=True)
    job_title = models.CharField(choices=JOB_TITLE_CHOICES, max_length=50)

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Sale(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    sum = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    def calculate_sum(self):
        total = sum(
            product.price for product in self.product.all()
        )

        self.sum = total
        self.save(update_fields=['sum'])