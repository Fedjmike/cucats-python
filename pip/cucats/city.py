from pygeocoder import Geocoder
from cucats.wrapper import Wrapper



def coordinates(city):
    return(Geocoder.geocode(city).coordinates)

def city(lat, lon):
    return(Geocoder.reverse_geocode(lat,lon))

def test(between):
    city1 = "London"
    city2 = "Moscow"
    lat = (coordinates(city1)[0] + coordinates(city2)[0])/2
    lon = (coordinates(city1)[1] + coordinates(city2)[1])/2
    answer = (city(lat, lon))
    their_answer = between("London", "Moscow")
    return str(their_answer) == str(answer)

# def between(city1,city2):
#   lat = (coordinates(city1)[0] + coordinates(city2)[0])/2
#   lon = (coordinates(city1)[1] + coordinates(city2)[1])/2
#   return(city(lat, lon)) 

class City (Wrapper):
    def __init__(self):
        instructions = """
        In this exercise, your task is to write a function 'between(city1, city2)' that:
        - Takes the names of two cities as input strings
        - Tells us what is at the point between the cities

        To help you do this, we're giving you two functions:
        - 'coordinates(city)': Takes the name of a city as input and gives you (latitude, longitude)
        - 'city(latitude,longitude)': Takes a latitude and a longitude as input and returns a string telling you what's at the point


        Hint: the coordinates of a point in the middle of two others are the averages of the coordinates of the two points.
        Hint: 'coordinates(city)' returns a pair of values. You can record this as:
        '(latitude, longitude) = coordinates(city)'
        """
        title = "Cities"
        Wrapper.__init__(self, title, test, instructions)
        print ("Cities loaded")