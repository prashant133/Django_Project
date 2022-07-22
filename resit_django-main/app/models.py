from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,  on_delete=models.CASCADE)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    username = models.CharField(max_length=200)
    profile_pic = models.FileField(
        upload_to='static/uploads', default='static/uploads/rog.png')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)+" "+str(self.phone)+" "+self.address+" "+self.email+" "+str(self.profile_pic)

PROVINCE_CHOICES = (
    ('Province No. 1', 'Province No. 1'),
    ('Province No. 2', 'Province No. 2'),
    ('Bagmati Province', 'Bagmati Province'),
    ('Gandaki Province', 'Gandaki Province'),
    ('Lumbini Province', 'Lumbini Province'),
    ('Karnali Province', 'Karnali Province'),
    ('Sudurpashchim Province', 'Sudurpashchim Province')
)

class Category_choices(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    marked_price = models.IntegerField()
    selling_price = models.IntegerField()
    brand = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category_choices, on_delete=models.CASCADE)
    product_image = models.ImageField(upload_to='productimg')

    def __str__(self):
        return str(self.id)+" "+self.title+" "+self.slug+" "+str(self.marked_price)+" "+str(self.selling_price)+" "+(self.brand)+" " + self.description + str(self.category)+" "+str(self.product_image)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    @property
    def total_cost(self):
        return self.quantity * self.product.selling_price

STATUS_CHOICES = (
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On The Way', 'On The Way'),
    ('Delievered', 'Delievered'),
    ('Cancel', 'Cancel')
)

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    province = models.CharField(choices=PROVINCE_CHOICES, max_length=50)
    zipcode = models.IntegerField()
    def __str__(self):
        return str(self.id)+" "+self.email+" "+self.name+" "+self.address+" "+self.city+" "+self.province+" "+str(self.zipcode)


class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    def __str__(self):
        return "Order: " + str(self.id)
    @property
    def total_cost(self):
        return self.quantity * self.product.selling_price
