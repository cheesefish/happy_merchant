extends "res://scripts/Inventory.gd"

func _ready():
	reset_point_items = {
		"Gold coin": [0, 5],
		"Silver coin": [1, 493], 
		"Copper coin": [2, 1150], 
		"Grain": [3, 555], 
		"Bread": [4, 370]
	}
	reset_items()
