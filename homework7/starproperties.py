# File: starproperties.py

import numpy as np

sigma = 5.670374419e-8 # Stefan-Boltzmann constant
G = 6.6743e-11 # Constant of Universal Gravitation

def star_radius(luminosity, temperature):
    """
    Calculates the radius of a star with its luminosity and surface temperature.
    """
    radius = np.sqrt(luminosity / (4 * np.pi * sigma * temperature ** 4)) # From Stefan Boltzman's Law (L = 4pir^2T^4 solving for R)
    return radius

def star_surface_area(radius):
    """
    Calculating the surface area of a star given its radius
    """
    area = 4 * np.pi * radius ** 2 # Assuming star is a perfect sphere
    return area

def gravitational_force(mass, distance):
    """
    Calculates the gravitational force between a star and an object at a given distance
    """
    force = G * mass / distance ** 2
    return force

def star_analysis(star_data):
    """
    Analyzes the properties of multiple stars using luminosity and temperature data to categorize them
    """
    results = []

    for star in star_data:
        luminosity, temperature = star
        radius = star_radius(luminosity, temperature)
        area = star_surface_area(radius)
        
        # Assuming an arbitrary mass and distance for demonstrational purposes
        mass = 1.989e30  # Approximate mass of the Sun in kg
        distance = radius + 1e8  # Distance from the surface of the star

        force = gravitational_force(mass, distance)

        if radius < 5e8:
            star_size_category = "Dwarf Star"
        elif 5e8 <= radius < 1e9:
            star_size_category = "Average Star"
        else:
            star_size_category = "Giant Star"

        results.append({
            "radius": radius,
            "star_surface_area": area,
            "star_gravitational_force": force,
            "star_size_category": star_size_category
        })

    return results
