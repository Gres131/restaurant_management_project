from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator
from products.models import Menu
class OrderStatus(models.Model):
    name = models.CharField(max_length=50,unique = True)

    def __str__(self):
        return self.name
# Create your models here.
class Order(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('PROCESSING', 'Processing'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]

    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="orders",
        verbose_name="Customer",
        help_text="The user who placed this order"
    )

    order_items = models.ManyToManyField(
        Menu,
        related_name="order_list",
        verbose_name="Order Items",
        help_text="Menu items included in this order"
    )

    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        verbose_name="Total Amount",
        help_text="Total price of all items in this order"
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='PENDING',
        verbose_name="order status",
        help_text="Current processing status of the order"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At",
        help_text="When the order was last updated"
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Updated At",
        help_text="When the order was last updated"
    )

    class Meta:
        ordering =['-created_at']
    
    def __str__(self):
        return f"Order #{self.id} - {self.customer} - {self.status}"
