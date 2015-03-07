# Pathfinding with dictionaries!

In this exercise, you'll write a program that can find a path between two cities using dictionaries. Grab the source file [here](cities.py/#L1).

In `cities.py` we've initialized a dictionary called `edges`. The keys of this dictionary are the names of cities, while the values are lists of cities that that city is connected to. For example,

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

## Starting out

In this program, we'll try to search for the destination 'depth first'. This means that we start with the origin (Seattle), pick a branch, and then keep following that branch as far as we can until we either:

* Find our destination.
* Come back to a city where we've already been.
* Reach a dead end.

For example, 

```
# Start off at Seattle
Seattle -> Minneapolis
Seattle -> Minneapolis -> Seattle # Have been here before, continue searching among the cities Minneapolis is connected to
Seattle -> Minneapolis -> Denver
Seattle -> Minneapolis -> Denver -> Seattle # Been here before
Seattle -> Minneapolis -> Denver -> Las Vegas
Seattle -> Minneapolis -> Denver -> Las Vegas -> San Fransisco
Seattle -> Minneapolis -> Denver -> Las Vegas -> San Fransisco -> Seattle # Been here before
Seattle -> Minneapolis -> Denver -> Las Vegas -> San Fransisco -> Las Vegas
Seattle -> Minneapolis -> Denver -> Las Vegas -> San Fransisco -> Los Angeles
Seattle -> Minneapolis -> Denver -> Las Vegas -> San Fransisco -> Los Angeles -> San Fransisco # And so on...
```

and you'd continue till you find Miami.

We're also going to break our problem down by making our function 'recursive'. This means our function will call itself. For example, if the path between Seattle and Las Vegas is:

```
Seattle -> Minneapolis -> Denver -> Las Vegas
```

this can be expressed as the path from Seattle to Denver followed by the path from Denver to Las Vegas:

```
Seattle -> Minneapolis
Minneapolis -> Denver -> Las Vegas
```

So, you need to write a function that:

* is a function of a `city_from` and a `city_to`.
* loops through the cities connected to `city_from`.
* returns `True` if it has reached the destination (i.e. if `city_to == destination`).
* calls itself with the current city we're looking at as `city_from`.
* keeps track of the cities you've already visited.
* breaks out of the loop (and then continues) if you've already visited `city_from`.
* returns `false` if we've looked at that city before.

It's harder than it sounds to get all of these right!