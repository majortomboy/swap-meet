from swap_meet.item import Item
class Electronics(Item):

    def __init__(self, category="", condition=0.0):
        self.category = "Electronics"
        self.condition = condition
        # refactor with super()

    def __str__(self):
        return "A gadget full of buttons and secrets."
