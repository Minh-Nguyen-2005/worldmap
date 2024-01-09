#Author: Minh Nguyen
#Date: 11/03/2023
#Purpose: City driver

# I adopted this idea from A20, this just proved how much application and value that your
# lectures and assignments have taught me. Thank you from the bottom of my heart for your CS1 class!

from cs1lib import *
from city import City
from quicksort import sort

mpressed = False
city = None
citi = None

#mouse initial coordinates
mx = 0
my = 0

WINDOW_W = 1024 # window width (pixels)
WINDOW_H = 512 # window height (pixels)

in_file = open("world_cities.txt", "r") # access the file world_cities.txt and "read" it
cities_list = [] # create a list of City objects

for line in in_file: # go through each line in world_cities.txt
    newline = line.strip() # strip away whitespace in the end of a string
    clauses = newline.split(",") # separate the information by the commas

    # the city constructor gives back a reference to a City object
    cities = City(clauses[0], clauses[1], clauses[2], clauses[3], clauses[4], clauses[5])
    cities_list.append(cities) # append that reference to the list
    # the list comprises 47913 references to City objects, one for each line in world_cities.txt after the loop.

in_file.close()

def compare_alpha(city1, city2): # compare the City objects by name in alphabetical order.
    return city1.name.lower() <= city2.name.lower()

def compare_population(city1, city2): # compare the City objects by population in decreasing order.
    return city1.population >= city2.population

def compare_latitude(city1, city2): # compare the City objects by latitude from south to north.
    return city1.latitude <= city2.latitude

city_alpha = open("cities_alpha.txt", "w") # access the file cities_alpha.txt and "write" on it
cities_list_alpha = sort(cities_list, compare_alpha) # sort the cities' name in the list in alphabetical order

for alp in cities_list_alpha:
    city_alpha.write(str(alp) + "\n")
# cities_alpha.txt contains the list of cities sorted alphabetically.
city_alpha.close()

city_latitude = open("cities_latitude.txt", "w") # access the file cities_latitude.txt and "write" on it
cities_list_latitude = sort(cities_list, compare_latitude) # sort the cities' latitude in the list from south to north

for lat in cities_list_latitude:
    city_latitude.write(str(lat) + "\n")
# cities_latitude.txt contains the list of cities sorted by latitude, from south to north.
city_latitude.close()

city_population = open("cities_population.txt", "w") # access the file cities_population.txt and "write" on it
cities_list_population = sort(cities_list, compare_population) # sort the cities' population in the list in decreasing order

for pop in cities_list_population:
    city_population.write(str(pop) + "\n")
# cities_population.txt contains the list of cities sorted by population, from most to least populous.
city_population.close()

img = load_image("wmmm.jpeg") # A16: extra credit #2

n = 1
def draw_map(): # main draw function
    global n, mpressed, mx, my, city, citi
    clear()
    draw_image(img, 0, 0) # display image file on the graphics window
    # The first parameter to draw_image refers to the object for the image returned by load_image.
    # The second and third parameters give the x- and y-coordinates of the upper left corner
    # of the image in the graphics window.

    # Show the most populous 100 cities from the cities_population.txt file, dynamically in an animation.
    i = 0
    while i < n:
        cities_list_population[i].draw(WINDOW_W/2, WINDOW_H/2) # draw each city's position on the image
        # cx, cy are constants, giving the pixel coordinates of the point at latitude 0 and longitude 0
        # which is the center of the projection.

# A16: extra credit #3
        # if you click the mouse on a certain city appears in the 100 most populous cities on the displayed
        # world map, its name will appear in yellow and stay there until you click another city
        if cities_list_population[i].is_clicked(mx, my, WINDOW_W/2, WINDOW_H/2) and mpressed == True:
            city = cities_list_population[i]

        # if you hover your mouse over a certain city appears in the 100 most populous cities on the displayed
        # world map, its name will appear in orange and disappear as soon as you move your mouse away from it
        if cities_list_population[i].is_clicked(mx, my, WINDOW_W/2, WINDOW_H/2) and mpressed == False:
            citi = cities_list_population[i]
            citi.draw_name(WINDOW_W/2, WINDOW_H/2, 1, 0.5, 0)

        i = i + 1

    if city != None: # how to have the clicked city's name stay
        city.draw_name(WINDOW_W/2, WINDOW_H/2, 1, 1, 0)

    if n <= 100:
        n += 1

def mmove(x, y):
    global mx, my
    mx = x
    my = y

def mpress(x, y):
    global mpressed, mx, my
    mpressed = True
    mx = x
    my = y

def mrelease(x, y):
    global mx, my, mpressed
    mx = x
    my = y
    mpressed = False

start_graphics(draw_map, width=WINDOW_W, height=WINDOW_H, framerate=10, mouse_move=mmove, mouse_press=mpress, mouse_release=mrelease)