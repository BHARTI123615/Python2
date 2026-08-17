
# Simple Inventory Management
inventory = {}

def add_item(name, qty):
    inventory[name] = inventory.get(name, 0) + qty

def remove_item(name, qty):
    if name in inventory and inventory[name] >= qty:
        inventory[name] -= qty
        if inventory[name] == 0:
            del inventory[name]

def show_inventory():
    for item, qty in inventory.items():
        print(f"{item}: {qty}")

# Example usage
add_item("Apples", 10)
add_item("Bananas", 5)
remove_item("Apples", 3)
show_inventory()
