extends Camera2D

const MOVE_SPEED = 500

const MAX_HORIZONTAL = 1000000
const MAX_VERTICAL = 1000000

func _process(delta):
	if is_current():
		_move_camera(delta)
		_constrict_camera()

func _move_camera(delta):
		var delta_position = Vector2.ZERO
		if Input.is_key_pressed(KEY_LEFT) or Input.is_key_pressed(KEY_A):
			delta_position += Vector2.LEFT
		if Input.is_key_pressed(KEY_RIGHT) or Input.is_key_pressed(KEY_D):
			delta_position += Vector2.RIGHT
		if Input.is_key_pressed(KEY_UP) or Input.is_key_pressed(KEY_W):
			delta_position += Vector2.UP
		if Input.is_key_pressed(KEY_DOWN) or Input.is_key_pressed(KEY_S):
			delta_position += Vector2.DOWN
		global_position += delta_position.normalized() * delta * MOVE_SPEED
	
func _constrict_camera():
	if(global_position[0] < -MAX_HORIZONTAL):
		global_position[0] = -MAX_HORIZONTAL
	elif(global_position[0] > MAX_HORIZONTAL):
		global_position[0] = MAX_HORIZONTAL
	if(global_position[1] < -MAX_VERTICAL):
		global_position[1] = -MAX_VERTICAL
	elif(global_position[1] > MAX_VERTICAL):
		global_position[1] = MAX_VERTICAL
