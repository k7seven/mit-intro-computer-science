from item import Item
from phone import Phone

item1 = Item("MyItem", 750)

item1.apply_increment(0.2)
item1.apply_discount()

print(item1.price)
