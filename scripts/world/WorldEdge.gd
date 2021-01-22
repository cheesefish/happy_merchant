class_name WorldEdge extends Node

var length
var hasStream = false

func init(node1, node2):
	node1.edges[node2.node_name] = self
	node2.edges[node1.node_name] = self
	length = (node1.position - node2.position).length()
	return self
