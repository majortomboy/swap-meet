from swap_meet.item import Item
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics
from swap_meet.clothing import Clothing
class Vendor:

    def __init__(self, inventory=None):
        if inventory == None:
            self.inventory = []
        else:
            self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return False
        else:
            self.inventory.remove(item)
        return item

    def get_by_category(self, category):
        item_list = []
        for item in self.inventory:
            if category == item.category:
                item_list.append(item)
        return item_list

    def swap_items(self, friend, my_item, their_item):
        if my_item not in self.inventory or their_item not in friend.inventory:
            return False
        else:
            friend.add(my_item)
            self.remove(my_item)
            self.add(their_item)
            friend.remove(their_item)
            return True

    def swap_first_item(self, friend):
        if not self.inventory or not friend.inventory:
            return False
        else:
            my_first_item = self.inventory[0]
            their_first_item = friend.inventory[0]
            self.add(their_first_item)
            friend.remove(their_first_item)
            friend.add(my_first_item)
            self.remove(my_first_item)
            return True

    def get_best_by_category(self, category):
        list_by_category = self.get_by_category(category)
        if list_by_category == None:
            return None
        else:
            best_item = list_by_category[0]
        # if category not in self.inventory:
        #     return None
        # how to I access the category of each item in the inventory?
        # for item in self.inventory:
        #     if item.category != category:
        #         return None
        for item in list_by_category:
            if item.condition >= best_item.condition:
                best_item = item
        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_list_by_category = self.get_by_category(my_priority)
        their_list_by_category = other.get_by_category(their_priority)
        if their_priority not in my_list_by_category or\
            my_priority not in their_list_by_category:
                return False
        else:
            my_item = self.get_best_by_category(their_priority)
            their_item = other.get_best_by_category(my_priority)
            self.swap_items(other, my_item, their_item)
            return True



# test

sid = Vendor()
# print(sid.inventory)
sid.add(Decor(condition=4))
sid.add(Electronics(condition=3))
sid.add(Clothing(condition=2))
#print(sid.inventory) # is there a way to get the __str__ for the entire list?

print(sid.inventory)
print(sid.get_by_category("Electronics"))
print(sid.get_best_by_category("Clothing"))

# ren = Vendor()
# print(ren.inventory)

# sid.swap_first_item(ren)
# print(ren.inventory)
# print(sid.inventory)
# for item in sid.inventory:
#     print(item)
