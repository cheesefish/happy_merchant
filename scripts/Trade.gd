extends Node

# The market's cut of each trade:
const market_margin = 0.1 # TODO: Does nothing right now

func _ready():
	# Connects item_clicked signals to their respective method below:
	$Player/Inventory.connect("item_clicked", self, "on_Player_Inventory_item_selected")
	$Market/Inventory.connect("item_clicked", self, "on_Market_Inventory_item_selected")

# Called when an item in the player inventory is clicked
func on_Player_Inventory_item_selected(item: InventoryItem):
	set_diff_and_transfer_item(item, $Market/Inventory, 1)

# Called when an item in the market inventory is clicked
func on_Market_Inventory_item_selected(item: InventoryItem):
	set_diff_and_transfer_item(item, $Player/Inventory, -1)

# Called when either of the inventories' items are clicked.
# Sets difference variable and then transfers item.
func set_diff_and_transfer_item(item, destination, balance_factor):
	var difference #number of items to be traded
	if Input.is_key_pressed(KEY_SHIFT):
		difference = 100 #number of items on shift-click
	elif Input.is_key_pressed(KEY_CONTROL):
		difference = 10 #number of items on ctrl-click
	else:
		difference = 1 #default number of items
	transfer_item(item, destination, balance_factor, difference)

# Handles the transfer of items from one inventory to another. (Prepare trade.)
# INPUT:	item			= clicked item
#			destination		= the destination inventory
#			balance_factor	= (1|-1); decides whether the transaction adds or 
#								subtracts from the trade balance
#			difference		= number of items to be traded
func transfer_item(item, destination, balance_factor, difference):
	
	# Sets the origin item's amount to its new amount:
	var amount_before = item.get_amount()
	var amount_after = amount_before - difference
	if amount_after <= 0: #handles too big trades
		item.set_amount(0)
		difference = amount_before
	else:
		item.set_amount(amount_after)
	
	# Sets the destination item amount to its new amount:
	if destination.items.has(item.get_name()):
		item = destination.items[item.get_name()]
		item.set_amount(item.get_amount() + difference)
	else: #handles cases when destination doesn't have the item type yet
		item = destination.add_item(item.get_name(), difference)
		item.true_amount = 0
	
	# Calculates and applies new trade balance:
	var market_value = item.get_value()
	var balance_difference = market_value * difference * balance_factor
	var balance_after = float($Center/BalanceValue.text) + balance_difference
	$Center/BalanceValue.text = str(balance_after) #changes the balance text
	
	# Only allows trade if balance is positive:
	$Center/ExchangeButton.disabled = balance_after < 0

# Aborts prepared trade by returning items and resetting trade balance.
func _on_ResetButton_pressed():
	reset_all_items_in_inventory($Market/Inventory)
	reset_all_items_in_inventory($Player/Inventory)
	$Center/BalanceValue.text = "0"

# Resets every item amount for the given inventory.
func reset_all_items_in_inventory(inventory: Inventory):
	var items_for_deletion = {} #list for adding items to be deleted
	
	# Resets item amounts and saves to items_for_deletion where appropriate:
	for item in inventory.items.values():
		if item.true_amount == 0:
			items_for_deletion[item.get_name()] = [inventory, item]
		else:
			item.set_amount(item.true_amount)
			
	# Deletes items created during the trade preparation / item transfer:
	for elem in items_for_deletion.values():
		elem[0].items.erase(elem[1].get_name())
		elem[1].delete()

# Executes prepared trade/transfers. Only possible with positive balance.
func _on_ExchangeButton_pressed():
	if not $Center/ExchangeButton.disabled:
		for item in $Market/Inventory.items.values():
			item.true_amount = item.get_amount()
		for item in $Player/Inventory.items.values():
			item.true_amount = item.get_amount()
		_on_ResetButton_pressed()
		$Center/ExchangeButton.disabled = true
