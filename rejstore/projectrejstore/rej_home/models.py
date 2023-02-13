from django.db import models
from django.urls import reverse


class Category(models.Model):
    categoryName = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(max_length=300, unique=True)
    categoryImage = models.ImageField(upload_to='category_img', blank=True)
    categoryDescription = models.TextField(blank=True)

    class Meta:
        ordering = ('categoryName',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('rej_home:products_by_category', args=[self.slug])

    def __str__(self):
        return '{}'.format(self.categoryName)


class Product(models.Model):
    productName = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(max_length=300, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    productImage = models.ImageField(upload_to='category_img', blank=True)
    productDescription = models.TextField(blank=True)
    productPrice = models.DecimalField(max_digits=20, decimal_places=2)
    productAvailable = models.BooleanField(default=True)
    productStock = models.IntegerField()
    productCreatedAt = models.DateField(auto_now_add=True)
    productUpdatedAt = models.DateField(auto_now=True)

    class Meta:
        ordering = ('productName',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def get_url(self):
        return reverse('rej_home:productDetails', args=[self.category.slug, self.slug])

    def __str__(self):
        return '{}'.format(self.productName)

