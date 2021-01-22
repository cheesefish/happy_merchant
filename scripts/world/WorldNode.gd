class_name WorldNode extends Node

var node_name
var position
var center #center of landmass
var edges = {} # key is name of opposite node
var areStreamsBridged = false
var town = null

func init(position:Vector2, node_name:String, center=null):
	self.position = position
	self.node_name = node_name
	self.center = center
	return self

func add_edge(edge: WorldEdge):
	edges[edge.get_other_node_name(node_name)] = edge
