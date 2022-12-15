from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=200)
    numberInStock = models.IntegerField(default=0)
    price = models.FloatField(default=0)

    def __str__(self):
        return f"{self.name} (£{self.price} each)"
    

class ShopingListItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    numberWanted = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.numberWanted} x {self.item.name}"

    def getTotalPrice(self):
        return self.item.price * self.numberWanted


class ShopingList(models.Model):
    items = models.ManyToManyField(ShopingListItem)
    totalPrice = models.FloatField(default=0)
    pubDate = models.DateTimeField('date published')

    def getTotalPrice(self):
        t = 0
        for item in self.items.all():
            t += item.getTotalPrice()
        return t

    def getTotalCount(self):
        t = 0
        for item in self.items.all():
            t += item.numberWanted
        return t