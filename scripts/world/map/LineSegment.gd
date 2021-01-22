class_name LineSegment extends Node2D

var vertex1
var vertex2
var color
var width

func init(v1:Vector2, v2:Vector2, color=Color.white, width=3.0):
	self.vertex1 = v1
	self.vertex2 = v2
	self.color = color
	self.width = width
	return self

func _draw():
	draw_line(vertex1, vertex2, color, width)
