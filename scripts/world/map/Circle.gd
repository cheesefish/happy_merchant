class_name Circle extends Node2D

var vertices = []
var color = PoolColorArray([Color.white])
var radius = 5.0
var num_points = 16

func init(position:Vector2, color=self.color[0], radius=self.radius, num_points=self.num_points):
	self.set_position(position)
	self.color = PoolColorArray([color])
	self.radius = radius
	self.num_points = num_points
	var k = 2*PI/num_points
	for i in range(0, num_points):
		vertices.append(Vector2(cos(i*k), sin(i*k)) * radius)
	return self

func _draw():
	draw_polygon(vertices, color)
