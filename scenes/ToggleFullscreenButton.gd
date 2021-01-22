extends Button

# Toggles to/from fullscreen when button is pressed.
func _pressed():
	OS.window_fullscreen = !OS.window_fullscreen
