extends "res://scripts/Inventory.gd"

func _ready():
	reset_point_items = {
		"Copper coin": [0, 51], 
		"Silver coin": [1, 2]
	}
	reset_items()
