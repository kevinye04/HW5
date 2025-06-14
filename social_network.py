# Name: ...
# CSE 160
# Homework 5

import utils  # noqa: F401, do not remove if using a Mac
import networkx as nx
import matplotlib.pyplot as plt
from operator import itemgetter


###
#  Problem 1a
###

def get_practice_graph():
    """Builds and returns the practice graph
    """
    practice_graph = nx.Graph()

    practice_graph.add_edge("A", "B")
    practice_graph.add_edge("A", "C")
    practice_graph.add_edge("B", "C")
    # (Your code for Problem 1a goes here.)
    practice_graph.add_edge("B", "D")
    practice_graph.add_edge("C", "D")  
    practice_graph.add_edge("C", "F")
    practice_graph.add_edge("D", "E")  
    practice_graph.add_edge("D", "F")
    return practice_graph


def draw_practice_graph(graph):
    """Draw practice_graph to the screen.
    """
    nx.draw_networkx(graph)
    plt.show()


###
#  Problem 1b
###

def get_romeo_and_juliet_graph():
    """Builds and returns the romeo and juliet graph
    """
    rj = nx.Graph()
    # (Your code for Problem 1b goes here.)
    characters = ["Nurse", "Friar Laurence", "Tybalt", "Benvolio", 
                  "Paris", "Mercutio", "Montague", "Capulet", 
                  "Escalus", "Juliet", "Romeo"]
    for character in characters:
        rj.add_node(character)

    rj.add_edge("Nurse", "Juliet")
    rj.add_edge("Friar Laurence", "Juliet")
    rj.add_edge("Friar Laurence", "Romeo")
    rj.add_edge("Tybalt", "Juliet")
    rj.add_edge("Tybalt", "Capulet")
    rj.add_edge("Benvolio", "Romeo")
    rj.add_edge("Benvolio", "Montague")
    rj.add_edge("Paris", "Escalus")
    rj.add_edge("Paris", "Capulet")
    rj.add_edge("Paris", "Mercutio")
    rj.add_edge("Mercutio", "Paris")
    rj.add_edge("Mercutio", "Escalus")
    rj.add_edge("Mercutio", "Romeo")
    rj.add_edge("Montague", "Escalus")
    rj.add_edge("Montague", "Romeo")
    rj.add_edge("Montague", "Benvolio")
    rj.add_edge("Capulet", "Juliet")
    rj.add_edge("Capulet", "Tybalt")
    rj.add_edge("Capulet", "Paris")
    rj.add_edge("Capulet", "Escalus")
    rj.add_edge("Escalus", "Paris")
    rj.add_edge("Escalus", "Mercutio")
    rj.add_edge("Escalus", "Montague")
    rj.add_edge("Escalus", "Capulet")
    rj.add_edge("Juliet", "Nurse")
    rj.add_edge("Juliet", "Tybalt")
    rj.add_edge("Juliet", "Capulet")
    rj.add_edge("Juliet", "Friar Laurence")
    rj.add_edge("Juliet", "Romeo")
    rj.add_edge("Romeo", "Friar Laurence")
    rj.add_edge("Romeo", "Benvolio")
    rj.add_edge("Romeo", "Montague")
    rj.add_edge("Romeo", "Mercutio")
    rj.add_edge("Romeo", "Juliet")
    return rj


def draw_rj(graph):
    """Draw the rj graph to the screen and to a file.
    """
    nx.draw_networkx(graph)
    plt.savefig("romeo-and-juliet.pdf")
    plt.show()


###
#  Problem 2
###

def friends(graph, user):
    """Returns a set of the friends of the given user, in the given graph.
    """
    # This function has already been implemented for you.
    # You do not need to add any more code to this (short!) function.
    return set(graph.neighbors(user))


def friends_of_friends(graph, user):
    """Find and return the friends of friends of the given user.

    Arguments:
        graph: the graph object that contains the user and others
        user: a string

    Returns: a set containing the names of all of the friends of
    friends of the user. The set should not contain the user itself
    or their immediate friends.
    """
    direct_friends = friends(graph, user)
    fof_set = set()
    
    for friend in direct_friends:
        for fof in graph.neighbors(friend):
            if fof != user:
                fof_set.add(fof)
    
    return fof_set - direct_friends



def common_friends(graph, user1, user2):
    """Finds and returns the set of friends that user1 and user2 have in common.

    Arguments:
        graph:  the graph object that contains the users
        user1: a string representing one user
        user2: a string representing another user

    Returns: a set containing the friends user1 and user2 have in common
    """
    friends1 = set(graph.neighbors(user1))
    friends2 = set(graph.neighbors(user2))
    common = set()
    
    for friend in friends1:
        if friend in friends2:
            common.add(friend)
    
    return common


def num_common_friends_map(graph, user):
    """Returns a map (a dictionary), mapping a person to the number of friends
    that person has in common with the given user. The map keys are the
    people who have at least one friend in common with the given user,
    and are neither the given user nor one of the given user's friends.
    Example: a graph called my_graph and user "X"
    Here is what is relevant about my_graph:
        - "X" and "Y" have two friends in common
        - "X" and "Z" have one friend in common
        - "X" and "W" have one friend in common
        - "X" and "V" have no friends in common
        - "X" is friends with "W" (but not with "Y" or "Z")
    Here is what should be returned:
      num_common_friends_map(my_graph, "X")  =>   { 'Y':2, 'Z':1 }

    Arguments:
        graph: the graph object that contains the user and others
        user: a string

    Returns: a dictionary mapping each person to the number of (non-zero)
    friends they have in common with the user
    """
    direct_friends = friends(graph, user)
    common_map = {}
    
    for person in graph.nodes():
        if person == user or person in direct_friends:
            continue
        
        common = len(common_friends(graph, user, person))
        if common > 0:
            common_map[person] = common
    
    return common_map


def num_map_to_sorted_list(map_with_number_vals):
    """Given a dictionary, return a list of the keys in the dictionary.
    The keys are sorted by the number value they map to, from greatest
    number down to smallest number.
    When two keys map to the same number value, the keys are sorted by their
    natural sort order for whatever type the key is, from least to greatest.

    Arguments:
        map_with_number_vals: a dictionary whose values are numbers

    Returns: a list of keys, sorted by the values in map_with_number_vals

    """
    w=sorted(map_with_number_vals.items(), key = itemgetter(0))
    q=sorted(w, key= itemgetter(1), reverse = True)
    number=[]
    for items in q:
        number.append(items[0])
    return number

def recommend_by_num_common_friends(graph, user):
    """
    Returns a list of friend recommendations for the user, sorted
    by number of friends in common.

    Arguments:
        graph: the graph object that contains the user and others
        user: a string

    Returns: A list of friend recommendations for the given user.
    The friend recommendation list consists of names/IDs of people in
    the graph who are not yet a friend of the given user.  The order
    of the list is determined by the number of common friends (people
    with the most common friends are listed first).  In the
    case of a tie in number of common friends, the names/IDs are
    sorted by their natural sort order, from least to greatest.
    """
    common_map = num_common_friends_map(graph, user)
    return num_map_to_sorted_list(common_map)



###
#  Problem 3
###

def influence_map(graph, user):
    """Returns a map (a dictionary) mapping from each person to their
    influence score, with respect to the given user. The map only
    contains people who have at least one friend in common with the given
    user and are neither the user nor one of the users's friends.
    See the assignment writeup for the definition of influence scores.
    """












    
def recommend_by_influence(graph, user):
    """Return a list of friend recommendations for the given user.
    The friend recommendation list consists of names/IDs of people in
    the graph who are not yet a friend of the given user.  The order
    of the list is determined by the influence score (people
    with the biggest influence score are listed first).  In the
    case of a tie in influence score, the names/IDs are sorted
    by their natural sort order, from least to greatest.
    """
    influence = influence_map(graph, user)
    items = list(influence.items())
    
    n = len(items)
    for i in range(n):
        for j in range(0, n - i - 1):
            val1 = items[j][1]
            val2 = items[j+1][1]
            key1 = items[j][0]
            key2 = items[j+1][0]
            
            if val1 < val2:
                items[j], items[j+1] = items[j+1], items[j]
            elif val1 == val2 and key1 > key2:
                items[j], items[j+1] = items[j+1], items[j]
    
    # 提取排序后的键
    sorted_keys = []
    for item in items:
        sorted_keys.append(item[0])
    
    return sorted_keys


###
#  Problem 5
###

def get_facebook_graph():
    """Builds and returns the facebook graph
    """

  

def main():
    practice_graph = get_practice_graph()
    # Comment out this line after you have visually verified your practice
    # graph.
    # Otherwise, the picture will pop up every time that you run your program.
    draw_practice_graph(practice_graph)

    rj = get_romeo_and_juliet_graph()
    # Comment out this line after you have visually verified your rj graph and
    # created your PDF file.
    # Otherwise, the picture will pop up every time that you run your program.
    draw_rj(rj)

    ###
    #  Problem 4
    ###

    print("Problem 4:")
    print()

    # (Your Problem 4 code goes here.)
    user = "Mercutio"
    
    # Get recommendations from both algorithms
    rec_by_common = recommend_by_num_common_friends(rj, user)
    rec_by_influence = recommend_by_influence(rj, user)
    
    # Find common recommendations
    common_recs = []
    for person in rec_by_common:
        if person in rec_by_influence:
            common_recs.append(person)
    
    # Find different recommendations
    diff_recs = []
    for person in rec_by_common:
        if person not in rec_by_influence:
            diff_recs.append(person)
    for person in rec_by_influence:
        if person not in rec_by_common:
            diff_recs.append(person)
    
    # Sort the results alphabetically
    common_recs.sort()
    diff_recs.sort()
    
    # Print results
    print("Same recommendations:", common_recs)
    print("Different recommendations:", diff_recs)

    ###
    #  Problem 5
    ###

    # (Your Problem 5 code goes here. Make sure to call get_facebook_graph.)

    # assert len(facebook.nodes()) == 63731
    # assert len(facebook.edges()) == 817090

    ###
    #  Problem 6
    ###
    print()
    print("Problem 6:")
    print()

    # (Your Problem 6 code goes here.)

    ###
    #  Problem 7
    ###
    print()
    print("Problem 7:")
    print()

    # (Your Problem 7 code goes here.)

    ###
    #  Problem 8
    ###
    print()
    print("Problem 8:")
    print()

    # (Your Problem 8 code goes here.)


if __name__ == "__main__":
    main()


###
#  Collaboration
###

# ... Write your answer here, as a comment (on lines starting with "#").
