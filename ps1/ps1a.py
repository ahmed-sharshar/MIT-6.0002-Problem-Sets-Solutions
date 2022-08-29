###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:
import time
from collections import OrderedDict
from ps1_partition import get_partitions
#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    cows={}
    dick=open(filename,'r')
    for i in dick:
        info=i.split(',')
        cows[info[0]] = int(info[1].rstrip())
    return cows
#print(load_cows('ps1_cow_data.txt'))
    
# Problem 2
cows=load_cows('ps1_cow_data.txt')
def greedy_cow_transport(cows,limit = 10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:
    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows
    Does not mutate the given dictionary of cows.
    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
   
    trips = []
    cows_copy = cows.copy()
    cows_sorted = OrderedDict(sorted(cows_copy.items(), reverse=True, key=lambda x: x[1]))       
    total_weight = 0
    list_index = 0
    while len(cows_sorted) > 0:        
        total_weight = 0  
        trips.append([])       
        for (cow, weight) in cows_sorted.copy().items():
            if total_weight + weight <= limit:
                trips[list_index].append(cow)
                total_weight = total_weight + weight
                del cows_sorted[cow]
        list_index += 1
    return trips  
#print (greedy_cow_transport(cows,limit=10))


#cows=load_cows('ps1_cow_data.txt')       
# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    trips = []
    cows_copy = cows.copy()
    cows_sorted = OrderedDict(sorted(cows_copy.items(), reverse=True, key=lambda x: x[1]))
    cow_partitions = get_partitions(cows_sorted) 
    successful_score = 0
    trip = 0
    for combo in cow_partitions:
        trip = 0
        find=[]
        for item in combo:
            weight = 0             
            successful_score = 0    
            for cow in item:
                if weight + cows_sorted[cow] <= limit and cow not in find:
                    weight = weight + cows_sorted[cow]
                    successful_score += 1
                    find.append(cow) 
                else:
                    break
                if  successful_score==len(item):
                     trip += 1
                if trip == len(combo):
                    if item not in trips:
                        trips.append(combo)
    minLength = len(trips[0])
    minTrip = trips[0]
    for trip in trips:
        if len(trip) < minLength:
            minLength = len(trip)
            minTrip = trip
    return list(minTrip)
#print(brute_force_cow_transport(cows,limit=10))
                    
# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    #cows = load_cows("ps1_cow_data.txt")
    start = time.time()
    print("Greedy algorithm is:",greedy_cow_transport(cows))
    end = time.time()
    print("greedy algorithm takes:",end - start, "seconds")
    start = time.time()
    print("Brute force algorithm is: ",brute_force_cow_transport(cows))
    end = time.time()
    print("Brute force algorithm: ",end - start, "seconds")

compare_cow_transport_algorithms()