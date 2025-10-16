# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from util import Stack

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"

    # Initialize fringe (a FIFO stack) with a starting state and empty path.
    fringe = util.Stack()                           
    fringe.push((problem.getStartState(), []))      # (state, path_to_current_state) 

    # Initialize set to track visited states
    visited = set()                                 

    while not fringe.isEmpty():
        currentState, actions = fringe.pop()

        # Check if current state in visited; avoid repeat visits & cycles
        if currentState in visited:                
            continue
        # Mark current state as visited
        visited.add(currentState)                  

        # Return action path if goal state reached
        if problem.isGoalState(currentState):      
            return actions
        
        # Process child nodes
        successors = problem.getSuccessors(currentState)
        for child, action, cost in successors:   
            # If not yet visited, push child to fringe & update current action path                   
            if child not in visited:                                
                fringe.push((child, actions + [action]))    

    # Return empty list if no solution
    return []           
 

def breadthFirstSearch(problem: SearchProblem):
    """
    Search the shallowest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    
    # Initialize the fringe (a FIFO queue) with the starting state and an empty path.
    # The items in the queue will be tuples: (state, pathToState)
    fringe = util.Queue()
    fringe.push((problem.getStartState(), []))

    # Initialize a set to keep track of visited states to prevent cycles
    # and redundant expansions.
    visited = set()

    # Loop until there are no more nodes to explore.
    while not fringe.isEmpty():
        # Dequeue the oldest node from the front of the fringe.
        currentState, actions = fringe.pop()

        # If we have already visited this state, skip it.
        if currentState in visited:
            continue

        # If this state is the goal, we have found a solution.
        if problem.isGoalState(currentState):
            return actions

        # Mark the current state as visited.
        visited.add(currentState)

        # Get the successors of the current state.
        for nextState, action, cost in problem.getSuccessors(currentState):
            # If the successor state has not been visited, add it to the fringe.
            if nextState not in visited:
                # The new path is the old path plus the new action.
                newActions = actions + [action]
                # Enqueue the new node to the back of the fringe.
                fringe.push((nextState, newActions))
                
    # If the fringe becomes empty and no solution was found, return an empty list.
    return []

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    # Initialize fringe (a priority queue) with a start state, path, and path cost (g)
    fringe = util.PriorityQueue()
    fringe.push((problem.getStartState(), [], 0), 0)      # (state, path, g)

    # Initialize a dict to keep track of visited states & lowest cost paths to each
    visited = {}

    # Loop until there are no more nodes to explore.
    while not fringe.isEmpty():
        # Pop the lowest cost node from the fringe.
        currentState, actions, g = fringe.pop()

        # If we have already expanded this state with cheaper g, skip it.
        if g > visited.get(currentState, float('inf')):
            continue

        # If this state is the goal, we have found a solution.
        if problem.isGoalState(currentState):
            return actions
        
        # Record best cost seen for this state
        visited[currentState] = g

        # Get the successors of the current state.
        for nextState, action, cost in problem.getSuccessors(currentState):
            # The new g = the old g + the new action cost.
            new_g = g + cost
            # If the successor state has not been visited with cheaper g, add it to the fringe.
            if new_g < visited.get(nextState, float('inf')):
                # Push the new node to the fringe.
                fringe.push((nextState, actions + [action], new_g), new_g)
                
    # If the fringe becomes empty and no solution was found, return an empty list.
    return []





def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    import util

def aStarSearch(problem, heuristic=nullHeuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.
    
    This function implements the A* search algorithm. It uses a Priority Queue
    for the fringe, where the priority is calculated as g(n) + h(n):
    g(n) = The actual cost of the path from the start node to node n.
    h(n) = The estimated cost from node n to the goal, provided by the heuristic.
    """
    # The fringe is a Priority Queue storing tuples of:
    # ((state, actions, cost), priority)
    fringe = util.PriorityQueue()

    # A set to store states that have already been expanded.
    visited = set()

    # Get the starting state and push it to the fringe.
    # The initial cost g(n) is 0. The priority is 0 + h(start).
    startState = problem.getStartState()
    fringe.push((startState, [], 0), 0 + heuristic(startState, problem))

    while not fringe.isEmpty():
        # Pop the node with the lowest priority (lowest g(n) + h(n)).
        currentState, actions, currentCost = fringe.pop()

        # If we've already found a cheaper path to this state, skip it.
        if currentState in visited:
            continue
        
        # Mark the state as visited. In A*, the first time we visit a node,
        # we have found the cheapest path to it.
        visited.add(currentState)

        # If we've reached the goal, return the actions to get here.
        if problem.isGoalState(currentState):
            return actions

        # Expand the node by adding its successors to the fringe.
        for nextState, action, stepCost in problem.getSuccessors(currentState):
            if nextState not in visited:
                # Calculate the new cost (g) to reach the successor.
                newCost = currentCost + stepCost
                # Calculate the new priority for the successor.
                priority = newCost + heuristic(nextState, problem)
                
                # Push the successor onto the fringe with its new priority.
                fringe.push((nextState, actions + [action], newCost), priority)

    # Return an empty list if no solution is found.
    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
