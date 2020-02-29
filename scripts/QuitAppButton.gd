extends Button

# Exists application when button is pressed.
func _pressed():
	self.get_tree().quit()
