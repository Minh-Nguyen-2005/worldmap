#Author: Minh Nguyen
#Date: 11/03/2023
#Purpose: City class

from cs1lib import *
from random import uniform

# constant variables
WINDOW_W = 1024 # window width (pixels)
WINDOW_H = 512 # window height (pixels)
RAD = 4 # radius

class City:
    def __init__(self, country_code, name, region, population, latitude, longitude):
        # takes six parameters (plus self) and stores each in the appropriate instance variable.
        self.countrycode = country_code # The city's country code, which is a two-letter string.
        self.name = name # The city's name, which is a string.
        self.region = region # The city's region, a two-character string.
        self.population = int(population) # The city's population, which is an int.
        self.latitude = float(latitude) # The city's latitude, which is a float.
        self.longitude = float(longitude) # The city's longitude, which is also a float.

    def __str__(self): # returns a string consisting of the city's name, population, latitude,
        # and longitude, separated by commas and with no spaces around the commas.
        return str(self.name) + "," + str(self.population) + "," + str(self.latitude) + "," + str(self.longitude)

    def draw(self, cx, cy): # takes the latitude and longitude of the city and draws it on world map.
        # latitudes (horizontal lines) range from -90 to +90,
        # longitudes (vertical lines) range from -180 to +180
        # scale self.latitude and self.longitude to the size of the image,
        # let's say px and py are the scaled values
        # real-life location on the map
        if -90 <= self.latitude <= 90 and -180 <= self.longitude <= 180:
            px = ((WINDOW_W/360) * self.longitude) + cx
            py = WINDOW_H - (((WINDOW_H/180) * self.latitude) + cy)

            disable_stroke()
            set_fill_color(uniform(0, 1), uniform(0, 1), uniform(0, 1))
            draw_circle(px, py, RAD) # call draw_circle(px, py, RAD) to draw that city in its

    def draw_name(self, cx, cy, r, g, b): # display the city's name on the map
        if -90 <= self.latitude <= 90 and -180 <= self.longitude <= 180:
            px = ((WINDOW_W/360) * self.longitude) + cx
            py = WINDOW_H - (((WINDOW_H/180) * self.latitude) + cy)
            enable_stroke()
            set_font_bold()
            set_stroke_color(r, g, b)
            draw_text(self.name, px, py)

    def is_clicked(self, x, y, cx, cy): # determine if the mouse is hovering over a city's position on the map
        if -90 <= self.latitude <= 90 and -180 <= self.longitude <= 180:
            px = ((WINDOW_W/360) * self.longitude) + cx
            py = WINDOW_H - (((WINDOW_H/180) * self.latitude) + cy)
            return px - RAD <= x <= px + RAD and py - RAD <= y <= py + RAD