from django.contrib import admin

from .models import Item, ShopingList, ShopingListItem

admin.site.register(Item)
admin.site.register(ShopingList)
admin.site.register(ShopingListItem)