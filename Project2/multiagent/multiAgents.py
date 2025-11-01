# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent
from pacman import GameState

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """


    def getAction(self, gameState: GameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState: GameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
        
        "*** YOUR CODE HERE ***"

        # Capsules (power pellets)
        currentCapsules = currentGameState.getCapsules()
        newCapsules = successorGameState.getCapsules()

        # Start from successor score (built-in rewards)
        score = successorGameState.getScore()
        #1) Food Incentive
        # If we actually ate food, reward it strongly
        if successorGameState.getNumFood() < currentGameState.getNumFood():
            score += 100.0

        # Otherwise, reward getting closer to *some* food
        foodList = newFood.asList()
        if foodList:
            closestFoodDist = min(manhattanDistance(newPos, f) for f in foodList)
            # Closer food ⇒ bigger bonus
            score += 10.0 / closestFoodDist

        # 2) GHOSTS (dangerous vs. scared)
        # Track how close a *dangerous* ghost is — this matters for capsules
        minDangerousGhostDist = float("inf")

        for ghost, scaredTime in zip(newGhostStates, newScaredTimes):
            ghostPos = ghost.getPosition()
            ghostDist = manhattanDistance(newPos, ghostPos)

            if scaredTime > 0:
                # Edible ghost: closer is better
                score += 5.0 / max(ghostDist, 1)
            else:
                # Dangerous ghost
                minDangerousGhostDist = min(minDangerousGhostDist, ghostDist)
                if ghostDist <= 1:
                    # Being right next to a live ghost is terrible
                    score -= 500.0
                else:
                    # Mild penalty for being kind of close
                    score -= 3.0 / ghostDist

        # 3) CAPSULE (POWER PELLET) LOGIC
        # Case A: we actually ate a capsule with this move
        if len(newCapsules) < len(currentCapsules):
            # Stronger than food, because it *flips* the ghost situation
            score += 150.0

        # Case B: we did NOT eat one, but there are capsules left:
        # if a dangerous ghost is near, prefer moving *toward* a capsule
        elif newCapsules:
            # distance from *new* position to the closest remaining capsule
            closestCapsuleDist = min(manhattanDistance(newPos, c) for c in newCapsules)

            # If a live ghost is nearby (say within 3 steps), push hard toward capsule
            if minDangerousGhostDist <= 3:
                score += 80.0 / closestCapsuleDist
            else:
                # Otherwise, still slightly prefer being closer to capsules
                score += 15.0 / closestCapsuleDist

        # 4) Penalize Stopping
        if action == Directions.STOP:
            score -= 10.0

        return score
def scoreEvaluationFunction(currentGameState: GameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)


class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState: GameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"
        numAgents = gameState.getNumAgents()

        def maxValue(state, depth):
            # Terminal or depth limit: evaluate
            if depth == self.depth or state.isWin() or state.isLose():
                return self.evaluationFunction(state)

            v = float('-inf')
            actions = state.getLegalActions(0)
            if not actions:
                return self.evaluationFunction(state)

            for a in actions:
                succ = state.generateSuccessor(0, a)
                v = max(v, minValue(succ, 1, depth))
            return v

        def minValue(state, agentIndex, depth):
            # Terminal: evaluate
            if state.isWin() or state.isLose():
                return self.evaluationFunction(state)

            v = float('inf')
            actions = state.getLegalActions(agentIndex)
            if not actions:
                return self.evaluationFunction(state)

            nextAgent = agentIndex + 1
            for a in actions:
                succ = state.generateSuccessor(agentIndex, a)
                if nextAgent == numAgents:
                    # Wraps back to Pacman: increment depth
                    v = min(v, maxValue(succ, depth + 1))
                else:
                    v = min(v, minValue(succ, nextAgent, depth))
            return v

        # Root: choose argmax action for Pacman
        bestVal = float('-inf')
        bestActions = []
        for a in gameState.getLegalActions(0):
            succ = gameState.generateSuccessor(0, a)
            val = minValue(succ, 1, 0)
            if val > bestVal:
                bestVal = val
                bestActions = [a]
            elif val == bestVal:
                bestActions.append(a)

        return random.choice(bestActions) if bestActions else Directions.STOP


class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState: GameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState: GameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState: GameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction
