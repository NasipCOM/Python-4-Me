

global cases
cases = int(input())
def duronto_eagle():
    planets_list = []
    for i in range(cases):
        num_of_planets = number_of_planets_inputs()
        farthest_planet = -1
        planet_index = -1

        for j in range(num_of_planets):
            x, y = inputs()
            distance = x ** 2 + y ** 2 # using p

            if distance > farthest_planet:
                farthest_planet = distance
                planet_index = j
        planets_list.append(planet_index)

    for i in range(cases):
        print("farthest planet ", i + 1, ": case ", planets_list[i] + 1)




def inputs():
    planet = input()
    planetList = [int(i) for i in planet.strip().split(' ')]
    return planetList


def number_of_planets_inputs():
    number_of_graphs = int(input())
    return number_of_graphs

duronto_eagle()