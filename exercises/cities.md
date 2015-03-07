# Pathfinding with dictionaries!

In this exercise, you'll write a program that can find a path between two cities using dictionaries. Grab the source file [here](cities.py/#L1).

## Starting out

In `cities.py` we've initialized a dictionary `edges`. The keys of the dictionary are the names of cities, while the values are lists of cities that that city is connected to. For example,

```
edges["Boston"]
```

would give you

```
["Chicago", "Washington DC", "New York"]
```

Your task is:

**Write a program to find a path from `origin` (`"Seattle"`) to `destination` (`"Miami"`).**

The problem can be approached in many ways- let your imagination run wild! Alternatively, a rough outline of a possible implementation will be given below.