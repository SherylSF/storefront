from django.db import models

# Create your models here.

class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()
    

class Collection(models.Model):
   title = models.CharField(max_length=255)
   featured_product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, related_name='+')


class Product(models.Model):
    title: models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_upadte = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    promotions = models.ManyToManyField(Promotion)

class Customer(models.Model):
    Membership_Bronze = 'B'
    Membership_Silver = 'S'
    Membership_Gold = 'G'

    MEMBERSHIP_CHOICES = [
        (Membership_Bronze, 'Bronze'),
        (Membership_Silver, 'Silver'),
        (Membership_Gold, 'Gold')
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=False)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default=Membership_Bronze)

    class Meta:
        db_table = 'store_customers'
        indexes = [
            models.Index(fields=['last_name', 'first_name'])
        ]


class Order(models.Model):
    placed_at = models.DateTimeField(auto_now_add=True)
    Payment_Pending = 'P'
    Payment_Complete = 'C'
    Payment_Failed = 'F'
    PAYMENT_STATUS_CHOICES = [
        (Payment_Pending, 'Pending'),
        (Payment_Complete, 'Complete'),
        (Payment_Failed, 'Failed')
    ]
    payment_status = models.CharField(max_length=1, choices=PAYMENT_STATUS_CHOICES, default=Payment_Pending)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

class Address(models.Model):
    street = models.CharField(max_length=255)
    city =  models.CharField(max_length=255)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)

class Order_Item(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()










