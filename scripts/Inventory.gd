class_name Inventory extends Control

var panel
var scroll_container
var grid_container
var top_labels = []

var items = {}
var items_backup = {}

signal item_clicked

func _init():
	self.size_flags_horizontal = SIZE_EXPAND_FILL
	self.size_flags_vertical = SIZE_EXPAND_FILL
	
	panel = Panel.new()
	panel.size_flags_horizontal = SIZE_EXPAND_FILL
	panel.size_flags_vertical = SIZE_EXPAND_FILL
	panel.anchor_right = 1
	panel.anchor_bottom = 1
	panel.margin_right = 0
	panel.margin_bottom = 0
	self.add_child(panel)
	
	scroll_container = ScrollContainer.new()
	scroll_container.scroll_horizontal_enabled = true
	scroll_container.size_flags_horizontal = SIZE_EXPAND_FILL
	scroll_container.size_flags_vertical = SIZE_EXPAND_FILL
	scroll_container.anchor_right = 1
	scroll_container.anchor_bottom = 1
	scroll_container.margin_right = 0
	scroll_container.margin_bottom = 0
	panel.add_child(scroll_container)
	
	grid_container = GridContainer.new()
	grid_container.size_flags_horizontal = SIZE_EXPAND_FILL
	grid_container.size_flags_vertical = SIZE_EXPAND_FILL
	scroll_container.add_child(grid_container)
	
	var label = Label.new()
	grid_container.add_child(label)
	top_labels.append(label)
	
	label = Label.new()
	label.text = "Name"
	label.size_flags_horizontal = SIZE_EXPAND_FILL
	grid_container.add_child(label)
	top_labels.append(label)
	
	label = Label.new()
	label.text = "Weight"
	label.size_flags_horizontal = SIZE_EXPAND_FILL
	grid_container.add_child(label)
	top_labels.append(label)
	
	label = Label.new()
	label.text = "Value"
	label.size_flags_horizontal = SIZE_EXPAND_FILL
	grid_container.add_child(label)
	top_labels.append(label)
	
	label = Label.new()
	label.text = "Amount"
	label.size_flags_horizontal = SIZE_EXPAND_FILL
	grid_container.add_child(label)
	top_labels.append(label)
	
	grid_container.columns = top_labels.size()

func on_item_clicked(item: InventoryItem):
	emit_signal("item_clicked", item)

func add_item(item_name: String, amount: int):
	var item = InventoryItem.new().init(self, grid_container, item_name, amount)
	items[item_name] = item
	return item
