extends HBoxContainer

const global_item_data = {
		"Gold coin": [0.05], 
		"Silver coin": [0.05], 
		"Copper coin": [0.05], 
		"Grain": [1], 
		"Bread": [0.5]
}

var difference

func _on_PlayerInventory_item_selected(index):
	var origin = $TradeRightContainer/PlayerInventory
	var destination = $TradeLeftContainer/MarketInventory
	set_diff_and_transfer_item(index, origin, destination, 1)

func _on_MarketInventory_item_selected(index):
	var origin = $TradeLeftContainer/MarketInventory
	var destination = $TradeRightContainer/PlayerInventory
	set_diff_and_transfer_item(index, origin, destination, -1)

func set_diff_and_transfer_item(index, origin, destination, factor):
	if Input.is_key_pressed(KEY_SHIFT):
		difference = 100
	elif Input.is_key_pressed(KEY_CONTROL):
		difference = 10
	else:
		difference = 1
	transfer_item(index, origin, destination, factor)

func transfer_item(index, origin: Inventory, destination: Inventory, factor):
	var name = origin.get_item_tooltip(index) #item name
	
	var amount_after = int( origin.get_item_text(index) ) - difference
	if amount_after > 0:
		origin.set_item_text( index, str(amount_after) )
	elif amount_after < 0:
		difference += amount_after
		transfer_item(index, origin, destination, factor)
		return #important to return here!
	else:
		origin.remove_inventory_item(name)
	
	if destination.has_inventory_item(name):
		index = destination.item_indicies[name]
		amount_after = int( destination.get_item_text(index) ) + difference
		destination.set_item_text(index, str(amount_after) )
	else:
		destination.add_inventory_item(name, difference)
	
	var value = $TradeLeftContainer/MarketInventory.local_item_data[name][0]
	var balance_difference = value * difference * factor
	var label = $TradeCenterContainer/TradeBalanceValue
	var balance_after = int(label.text) + balance_difference
	label.text = str(balance_after)

func _on_TradeResetButton_pressed():
	$TradeRightContainer/PlayerInventory.reset_items()
	$TradeLeftContainer/MarketInventory.reset_items()
	$TradeCenterContainer/TradeBalanceValue.text = "0"
