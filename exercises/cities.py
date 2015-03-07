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
destination = "Miami"

visited = [origin]

# Your function goes here!