class_name Item extends Control

var parent
var grid

var icon
var name_label
var weight_label
var value_label
var amount_label
var overlay

var hidden_overlay_theme
var visible_overlay_theme

func init(parent, grid: Control, name, amount):
	var tex_path = "res://items/icons/" + String(name).to_lower() + "_64.png"
	var weight = 0.0
	var value = 0.1
	hidden_overlay_theme = load("res://themes/item_overlay_hidden.tres")
	visible_overlay_theme = load("res://themes/item_overlay_visible.tres")
	self.parent = parent
	self.grid = grid
	
	icon = TextureRect.new()
	icon.texture = load(tex_path)
	grid.add_child(icon)
	
	name_label = Label.new()
	name_label.text = name
	name_label.align = Label.ALIGN_LEFT
	name_label.valign = Label.ALIGN_CENTER
	grid.add_child(name_label)
	
	weight_label = Label.new()
	weight_label.text = str(weight)
	weight_label.align = Label.ALIGN_CENTER
	weight_label.valign = Label.ALIGN_CENTER
	grid.add_child(weight_label)
	
	value_label = Label.new()
	value_label.text = str(value)
	value_label.align = Label.ALIGN_CENTER
	value_label.valign = Label.ALIGN_CENTER
	grid.add_child(value_label)
	
	amount_label = Label.new()
	amount_label.text = str(amount)
	amount_label.align = Label.ALIGN_CENTER
	amount_label.valign = Label.ALIGN_CENTER
	grid.add_child(amount_label)
	
	overlay = Panel.new()
	icon.add_child(overlay)
	overlay.anchor_right = 1
	overlay.anchor_bottom = 1
	overlay.margin_right = ProjectSettings.get_setting("display/window/size/width") #ugh
	overlay.margin_bottom = 0
	overlay.connect("gui_input", self, "on_gui_input")
	overlay.theme = hidden_overlay_theme

func delete():
	grid.remove_child(icon)
	grid.remove_child(name_label)
	grid.remove_child(weight_label)
	grid.remove_child(value_label)
	grid.remove_child(amount_label)

func on_gui_input(event: InputEvent):
	if event is InputEventMouseButton && event.button_index == BUTTON_LEFT:
		if event.pressed:
			overlay.theme = visible_overlay_theme
		else:
			overlay.theme = hidden_overlay_theme
			parent.on_item_clicked(self)

func get_name() -> String:
	return str(name_label.text)

func get_weight() -> float:
	return float(weight_label.text)

func get_value() -> float:
	return float(value_label.text)

func get_amount() -> int:
	return int(amount_label.text)

func set_name(new_name: String):
	name_label.text = str(new_name)

func set_weight(new_weight: float):
	weight_label.text = str(new_weight)

func set_value(new_value: float):
	value_label.text = str(new_value)

func set_amount(new_amount: int):
	amount_label.text = str(new_amount)
