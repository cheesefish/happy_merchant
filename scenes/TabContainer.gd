extends TabContainer

func _on_TabContainer_tab_selected(tab):
	var camera_control = $"Map scene/Viewport/Camera2D"
	var is_map_scene = get_tab_control(tab) == $"Map scene"
	camera_control._set_current(is_map_scene)
	#camera_control.set_process(is_map_scene)
