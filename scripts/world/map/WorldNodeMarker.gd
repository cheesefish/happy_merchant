class_name WorldNodeMarker extends Node2D

var circle
var node_name:String

func init(node:WorldNode, color=self.color[0], radius=self.radius, num_points=self.num_points):
	set_position(node.position)
	circle = Circle.new().init(Vector2.ZERO, color, radius, num_points)
	add_child(circle)
	self.node_name = node.node_name
	var label = Label.new()
	label.set_position(Vector2.RIGHT * radius)
	label.set_text(node_name)
	add_child(label)
	return self
