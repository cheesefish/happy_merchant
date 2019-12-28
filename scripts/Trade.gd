extends Node

var difference

func _ready():
	$Player/Inventory.connect("item_clicked", self, "on_Player_Inventory_item_selected")
	$Market/Inventory.connect("item_clicked", self, "on_Market_Inventory_item_selected")

func on_Player_Inventory_item_selected(item: Item):
	var origin = $Player/Inventory
	var destination = $Market/Inventory
	set_diff_and_transfer_item(item, origin, destination, 1)

func on_Market_Inventory_item_selected(item: Item):
	var origin = $Market/Inventory
	var destination = $Player/Inventory
	set_diff_and_transfer_item(item, origin, destination, -1)

func set_diff_and_transfer_item(item, origin, destination, factor):
	if Input.is_key_pressed(KEY_SHIFT):
		difference = 100
	elif Input.is_key_pressed(KEY_CONTROL):
		difference = 10
	else:
		difference = 1
	transfer_item(item, origin, destination, factor)

func transfer_item(item: Item, origin: Inventory, destination: Inventory, factor):
	var item_name = item.get_name()
	var amount_after = item.get_amount() - difference
	
	if amount_after > 0:
		item.set_amount(amount_after)
	elif amount_after < 0:
		difference += amount_after
		transfer_item(item, origin, destination, factor)
		return #important to return here!
	else:
		origin.remove_item(item_name)
	
	if destination.has_item(item_name):
		destination.add_to_item_amount(item_name, difference)
	else:
		destination.add_item(item_name, difference)
	
	var value = item.get_value()
	var balance_difference = value * difference * factor
	var label = $Center/BalanceValue
	var balance_after = float(label.text) + balance_difference
	label.text = str(balance_after)

func on_TradeResetButton_pressed():
	$Market/Inventory.reset_items()
	$Player/Inventory.reset_items()
	$Center/BalanceValue.text = "0"
