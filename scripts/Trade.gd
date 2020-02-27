extends Node

const market_margin = 0.1

func _ready():
	$Player/Inventory.connect("item_clicked", self, "on_Player_Inventory_item_selected")
	$Market/Inventory.connect("item_clicked", self, "on_Market_Inventory_item_selected")

func on_Player_Inventory_item_selected(item: InventoryItem):
	set_diff_and_transfer_item(item, $Player/Inventory, $Market/Inventory, 1)

func on_Market_Inventory_item_selected(item: InventoryItem):
	set_diff_and_transfer_item(item, $Market/Inventory, $Player/Inventory, -1)

func set_diff_and_transfer_item(item, origin, destination, balance_factor):
	var difference
	if Input.is_key_pressed(KEY_SHIFT):
		difference = 100
	elif Input.is_key_pressed(KEY_CONTROL):
		difference = 10
	else:
		difference = 1
	transfer_item(item, origin, destination, balance_factor, difference)

func transfer_item(item, origin, destination, balance_factor, difference):
	var amount_before = item.get_amount()
	if amount_before == 0: return
	
	var amount_after = amount_before - difference
	if amount_after <= 0:
		if item.true_amount == 0:
			origin.items.erase(item.get_name())
			item.delete()
		else:
			item.set_amount(0)
		difference = amount_before
	else:
		item.set_amount(amount_after)
	
	var item_name = item.get_name()
	if destination.items.has(item_name):
		item = destination.items[item_name]
		item.set_amount(item.get_amount() + difference)
	else:
		item = destination.add_item(item_name, difference)
		item.true_amount = 0
	
	var market_value = item.get_value()# * (1 - balance_factor * market_margin)
	var balance_difference = market_value * difference * balance_factor
	var balance_after = float($Center/BalanceValue.text) + balance_difference
	$Center/BalanceValue.text = str(balance_after)
	$Center/ExchangeButton.disabled = balance_after < 0

func _on_ResetButton_pressed():
	var items_for_deletion = {}
	for item in $Market/Inventory.items.values():
		if item.true_amount == 0:
			items_for_deletion[item.get_name()] = [$Market/Inventory, item]
		else:
			item.set_amount(item.true_amount)
	for item in $Player/Inventory.items.values():
		if item.true_amount == 0:
			items_for_deletion[item.get_name()] = [$Player/Inventory, item]
		else:
			item.set_amount(item.true_amount)
	for elem in items_for_deletion.values():
		elem[0].items.erase(elem[1].get_name())
		elem[1].delete()
	$Center/BalanceValue.text = "0"

func _on_ExchangeButton_pressed():
	if not $Center/ExchangeButton.disabled:
		for item in $Market/Inventory.items.values():
			item.true_amount = item.get_amount()
		for item in $Player/Inventory.items.values():
			item.true_amount = item.get_amount()
		_on_ResetButton_pressed()
		$Center/ExchangeButton.disabled = true
		
