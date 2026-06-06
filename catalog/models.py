from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории")
    
    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    name = models.CharField(max_length=200, verbose_name="Название товара")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    image_url = models.URLField(blank=True, verbose_name="Ссылка на картинку")

    def __str__(self):
        return self.name

class Order(models.Model):
    order_number = models.CharField(max_length=10, unique=True, verbose_name="Номер заказа")
    phone = models.CharField(max_length=20, verbose_name="Телефон клиента")
    details = models.TextField(verbose_name="Состав заказа")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"Заказ №{self.order_number}"