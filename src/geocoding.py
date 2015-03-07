from pygeocoder import Geocoder
import geomaths

def coordinates(city):
    return(Geocoder.geocode(city).coordinates)

edges = {}

edges["Seattle"] = ["Minnerapolis", "Denver", "San Fransisco"]
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

def distances_dictionary(city_from, cities):
	distances = {}
	for city_to in cities:
		distances[city_to] = geomaths.distance(coordinates(city_from), coordinates(city_to))
	return distances

# def naive_pathfinding(edges, city_from, city_to):
	
# 	for cities in edges[city_from]:


print(distances_dictionary("Seattle", edges["Seattle"]))

