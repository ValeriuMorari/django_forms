from django.db import models


class Size(models.Model):
    title = models.CharField(max_length=100)
    objects = models.Manager()

    def __str__(self):
        return self.title


class Pizza(models.Model):
    objects = models.Manager()
    topping1 = models.CharField(max_length=100)
    topping2 = models.CharField(max_length=100)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.topping1}_{self.topping2}_{self.size}"
