from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name

    class Meta:
        db_table = "category"
        verbose_name = "Category"
        verbose_name_plural = "Categories"



