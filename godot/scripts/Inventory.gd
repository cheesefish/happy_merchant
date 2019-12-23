class_name Inventory extends ItemList

var icon_path = "res://items/icons/"
var local_item_data = {}
var item_indicies = {}

var reset_point_items = {}

func _ready():
	local_item_data = {
		"Gold coin": [100], 
		"Silver coin": [10], 
		"Copper coin": [1], 
		"Grain": [2], 
		"Bread": [2]
	}

func reset_items():
	clear()
	for name in reset_point_items.keys():
		var texture = load(icon_path + String(name).to_lower() + ".png")
		var index = reset_point_items[name][0]
		var amount = reset_point_items[name][1]
		add_item( str(amount), texture )
		set_item_tooltip(index, name)
		item_indicies[name] = index

func add_inventory_item(name, amount):
	var texture = load(icon_path + String(name).to_lower() + ".png")
	var index = get_item_count()
	add_item(str(amount), texture)
	set_item_tooltip(index, name)
	item_indicies[name] = index

func remove_inventory_item(name):
	var index = item_indicies[name]
	remove_item(index)
	item_indicies.erase(name)
	for name in item_indicies.keys():
		if item_indicies[name] > index:
			item_indicies[name] -= 1

func has_inventory_item(item_name):
	return item_indicies.has(item_name)
