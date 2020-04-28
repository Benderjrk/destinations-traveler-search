destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]


def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index

def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index
  
test_destination_index = get_traveler_location(test_traveler)

# print("LA Index", get_destination_index("Los Angeles, USA"))
# print("Paris Index", get_destination_index("Paris, France"))
# print("India", get_destination_index("Hyderabad, India"))

attractions = [[] for destination in destinations]

def add_attractions(destination, attraction):
  try:
    # getting the index in the destiation list
    destination_index = get_destination_index(destination)
    # getting the list in [[],[],[],[],[]]
    attractions_for_destination = attractions[destination_index]
    
    attractions_for_destination.append(attraction)
    return
    
  except ValueError:
    print(destination + " doesn't exist in our destinations")
    return
  
add_attractions("Los Angeles, USA", ['Venice Beach', ['beach']])


add_attractions("Paris, France", ["the Louvre", ["art", "museum"]])
add_attractions("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attractions("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attractions("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attractions("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attractions("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attractions("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attractions("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attractions("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attractions("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

def find_attractions(destination, interests):
  destination_index = get_destination_index(destination)
    # getting the list in [[],[],[],[],[]]
  attractions_in_city = attractions[destination_index]
  # print('attraction in city', attractions_in_city)
  
  # attractions that match our interests
  attractions_with_interest = []
  # print('attaction that match interersts', attractions_with_interest)
  for i in range(len(attractions_in_city)):
     # print('index', i)
    
    possible_attraction = attractions_in_city[i]
    
    attraction_tags = possible_attraction[1]
    # print('attraction tags', attraction_tags)
    
    for t in range(len(interests)):
      if interests[t] in attraction_tags:
        if possible_attraction not in attractions_with_interest:
          attractions_with_interest.append(possible_attraction[0])
      else:
        continue
  
  return attractions_with_interest

la_arts = find_attractions("Los Angeles, USA", ["art"])
# print(la_arts)

def get_attractions_for_traveler(traveler):
  traveler_destination, traveler_interests = traveler[1], traveler[2]
  
  traveler_attractions = find_attractions(traveler_destination, traveler_interests)
  
  interests_string = "Hi " + traveler[0] + ", we think you'll like these places around " + traveler_destination + "."
  
  for i in range(len(traveler_attractions)):
    if i == len(traveler_attractions) - 1:
      interests_string = interests_string + " " + traveler_attractions[i] + "."
    elif i == 0:
      interests_string = interests_string + " " + traveler_attractions[i] + ","
    
  return interests_string

test_user_get_attractions = get_attractions_for_traveler(test_traveler)

smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])

print(test_user_get_attractions)
print("\n")
print(smills_france)

