class_name WorldClass extends Node

const WORLD_SCALE = 1

var itemNames = [] # list of all types of items in the world
var nodes = {} # world nodes (settlements)

func _init():
	var s = WORLD_SCALE
	make_island(Vector2(0,0)*s, 500, 12, 1, 0.6*s, 567898765456743)
	make_island(Vector2(-250,150)*s, 50, 6, 5, 0.4*s, 4343434322434324343)
	make_sea_routes()
	make_map()

func make_island(center:Vector2, radius, num_nodes, rand_scale=1.0, scale=1.0, rng_seed=1234567890):	
	var rng = RandomNumberGenerator.new()
	rng.seed = rng_seed
	var coast_nodes = []
	var k = 2*PI/num_nodes
	var m = nodes.size()
	for i in range(0, num_nodes):
		var position = Vector2(cos(i*k), sin(i*k)) * radius
		position *= 0.5 + rng.randf() * rand_scale
		position *= scale
		position += center
		position
		var node_name = "c" + str(m + i)
		var node = WorldNode.new().init(position, node_name, center)
		nodes[node_name] = node
		coast_nodes.append(node)
	var polygon = PoolVector2Array()
	for node in coast_nodes:
		polygon.append(node.position)
	var land_polygon = Polygon2D.new()
	land_polygon.set_polygon(polygon)
	land_polygon.set_color(Color.forestgreen)
	add_child(land_polygon)
	for i in range(0, coast_nodes.size()):
		var node1 = coast_nodes[i-1]
		var node2 = coast_nodes[i]
		WorldEdge.new().init(node1, node2)
		add_child(LineSegment.new().init(node1.position, node2.position, Color.blue))
	for node in coast_nodes:
		add_child(WorldNodeMarker.new().init(node, Color.white))

func make_sea_routes():
	for to_key in nodes.keys():
		var to_node = nodes[to_key]
		print([to_key] + to_node.edges.keys())
		for from_key in nodes.keys():
			if(from_key in [to_key] + to_node.edges.keys()):
				continue
			var from_node = nodes[from_key]
			if is_legal_sea_route(from_node, to_node):
				WorldEdge.new().init(from_node, to_node)
				add_child(LineSegment.new().init(from_node.position, to_node.position, Color.blue))

func is_legal_sea_route(from_node, to_node):
	for collision_node in nodes.values():
		if does_line_segments_intersect(from_node, to_node, collision_node):
			return false
	return true

# https://stackoverflow.com/questions/563198/how-do-you-detect-where-two-line-segments-intersect
func does_line_segments_intersect(from_node, to_node, collision_node):
	var p = from_node.position
	var r = p.direction_to(to_node.position) * p.distance_to(to_node.position)
	var q = collision_node.center
	var s = q.direction_to(collision_node.position) * q.distance_to(collision_node.position)
	if r.cross(s) != 0:
		var t = (q - p).cross(s) / r.cross(s)
		var u = (q - p).cross(r) / r.cross(s)
		return 0 < t and t < 1 and 0 < u and u < 1
	elif (q - p).cross(r) == 0:
		return true
	return false

func redraw_nodes():
	for node in nodes.values():
		add_child(WorldNodeMarker.new().init(node, Color.white))

func make_map():
	for node in nodes.values():
		for name2 in node.edges.keys():
			var v1 = node.position
			var v2 = nodes[name2].position
			add_child()
			
