from pygeocoder import Geocoder
import geomaths

def coordinates(city):
    return(Geocoder.geocode(city).coordinates)

edges = {}

edges["Seattle"] = ["Minneapolis", "Denver", "San Fransisco"]
edges["San Fransisco"] = ["Seattle", "Las Vegas", "Los Angeles"]
edges["Los Angeles"] = ["San Fransisco", "Las Vegas"]
edges["Las Vegas"] = ["San Fransisco", "Los Angeles", "Denver", "Dallas"]
edges["Denver"] = ["Seattle", "Las Vegas", "Minneapolis", "Dallas"]
edges["Minneapolis"] = ["Seattle", "Denver", "Dallas", "Chicago"]
edges["Dallas"] = ["Las Vegas", "Denver", "Minneapolis", "Washington DC", "Miami"]
edges["Chicago"] = ["Minneapolis", "Washington DC", "Boston"]
edges["Washington DC"] = ["Dallas", "Chicago", "Boston", "New York", "Miami"]
edges["Miami"] = ["Dallas", "Washington DC", "New York"]
edges["New York"] = ["Miami", "Washington", "Boston"]
edges["Boston"] = ["Chicago", "Washington DC", "New York"]

origin = "Seattle"
destination = "Washington DC"

def distances_dictionary(city_from, cities):
	distances = {}
	for city_to in cities:
		distances[city_to] = geomaths.distance(coordinates(city_from), coordinates(city_to))
	return distances

visited = [origin]

def naive_pathfinding(city_from, city_to):
	for city in edges[city_from]:
		print(visited, city)
		if city == city_to:
			print("dank")
			return True
		elif city in visited:
			continue
		else:
			visited.append(city)
			if naive_pathfinding(city, city_to):
				return True
			else:
				continue
	print("not dank", visited)
	return False

print(naive_pathfinding("Seattle", "Miami"))

# print(distances_dictionary("Seattle", edges["Seattle"]))

