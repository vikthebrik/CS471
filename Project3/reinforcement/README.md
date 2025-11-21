# Project 3: Reinforcement Learning

**University of Oregon CS 471 Fall 2025**  
**Implemented by:** Madeline Luu and Vikram Thirumaran

---

## Overview

This project implements value iteration and Q-learning algorithms for reinforcement learning. The implementations are tested on Gridworld (from class), a simulated robot controller (Crawler), and Pacman.

The project explores fundamental RL concepts including:
- Value iteration for known MDPs
- Q-learning for unknown environments
- Epsilon-greedy exploration strategies
- Approximate Q-learning with feature extraction

---

## Project Structure

### Files You Should Edit
- **`valueIterationAgents.py`** - Implementation of value iteration agent
- **`qlearningAgents.py`** - Implementation of Q-learning agents (Gridworld, Crawler, Pacman)
- **`analysis.py`** - Answers to policy analysis questions

### Key Implementation Files
- **`learningAgents.py`** - Base classes (`ValueEstimationAgent`, `ReinforcementAgent`)
- **`mdp.py`** - Markov Decision Process interface
- **`gridworld.py`** - Gridworld environment implementation
- **`featureExtractors.py`** - Feature extraction for approximate Q-learning
- **`util.py`** - Utility functions (including `Counter` and `flipCoin`)

### Test Files
- **`autograder.py`** - Autograder for all questions
- **`test_cases/`** - Test cases for each question (q1-q6)

---

## Running the Project

### Run All Tests
```bash
cd reinforcement
python autograder.py
```

### Run Specific Question
```bash
python autograder.py -q q1    # Value Iteration
python autograder.py -q q2    # Policies
python autograder.py -q q3    # Q-Learning
python autograder.py -q q4    # Epsilon Greedy
python autograder.py -q q5    # Q-Learning and Pacman
python autograder.py -q q6    # Approximate Q-Learning
```

### Run Specific Test Case
```bash
python autograder.py -t test_cases/q3/1-tinygrid
```

### Run Without Graphics (Faster)
```bash
python autograder.py --no-graphics
```

### Run Silently (Muted Output)
```bash
python autograder.py --mute
```

---

## Interactive Testing

### Gridworld
```bash
# Manual control
python gridworld.py -m

# Value iteration agent
python gridworld.py -a vi -i 100

# Q-learning agent
python gridworld.py -a q -k 100

# Q-learning with different epsilon values
python gridworld.py -a q -k 100 --noise 0.0 -e 0.1
python gridworld.py -a q -k 100 --noise 0.0 -e 0.9
```

### Crawler Robot
```bash
python crawler.py
```

### Pacman
```bash
# Q-learning Pacman (small grid)
python pacman.py -p PacmanQAgent -x 2000 -n 2010 -l smallGrid

# Approximate Q-learning Pacman (medium grid)
python pacman.py -p ApproximateQAgent -a extractor=SimpleExtractor -x 50 -n 60 -l mediumGrid

# Watch training games
python pacman.py -p PacmanQAgent -n 10 -l smallGrid -a numTraining=10
```

---

## Questions Breakdown

### Q1: Value Iteration (6 points)
**File:** `valueIterationAgents.py`

Implements value iteration for solving known MDPs:
- **`runValueIteration()`** - Runs batch value iteration for k iterations
- **`computeQValueFromValues(state, action)`** - Computes Q-value from value function
- **`computeActionFromValues(state)`** - Computes best action from value function

**Key Concepts:**
- Batch value iteration: V_{k+1} computed from fixed V_k (not updated in-place)
- Bellman equation: V(s) = max_a Σ_{s'} T(s,a,s') [R(s,a,s') + γV(s')]
- Q-values: Q(s,a) = Σ_{s'} T(s,a,s') [R(s,a,s') + γV(s')]

### Q2: Policies (5 points)
**File:** `analysis.py`

Answers policy analysis questions by setting appropriate parameters:
- Discount factor (γ)
- Noise (transition probability uncertainty)
- Living reward

**Questions:**
- `question2a()` - Prefer close exit, risking cliff
- `question2b()` - Prefer close exit, avoiding cliff
- `question2c()` - Prefer distant exit, risking cliff
- `question2d()` - Prefer distant exit, avoiding cliff
- `question2e()` - Avoid both exits and cliff (never terminate)

### Q3: Q-Learning (6 points)
**File:** `qlearningAgents.py` - `QLearningAgent` class

Implements Q-learning for unknown MDPs:
- **`getQValue(state, action)`** - Returns Q(s,a), defaulting to 0.0 for unseen states
- **`computeValueFromQValues(state)`** - Returns max_a Q(s,a)
- **`computeActionFromQValues(state)`** - Returns argmax_a Q(s,a) with random tie-breaking
- **`getAction(state)`** - Epsilon-greedy action selection
- **`update(state, action, nextState, reward)`** - Q-learning update rule

**Q-Learning Update:**
```
Q(s,a) ← Q(s,a) + α[r + γ·max_{a'} Q(s',a') - Q(s,a)]
```

**Key Features:**
- Off-policy learning (learns optimal policy while exploring)
- Random tie-breaking for optimal exploration
- Handles unseen actions (Q-value = 0.0)

### Q4: Epsilon Greedy (2 points)
**File:** `qlearningAgents.py` - `QLearningAgent.getAction()` method

Tests that epsilon-greedy action selection is correctly implemented:
- With probability ε: choose random action (explore)
- With probability 1-ε: choose best action (exploit)

This is automatically tested by the Q-learning implementation in Q3.

### Q5: Q-Learning and Pacman (2 points)
**File:** `qlearningAgents.py` - `PacmanQAgent` class

Applies Q-learning to Pacman on small grids:
- Extends `QLearningAgent` with Pacman-specific defaults
- `epsilon=0.05, alpha=0.2, gamma=0.8`
- Trains for 2000 episodes, tests for 100 episodes
- Must win ≥70% of test games

**Important Fix:**
- Random tie-breaking in `computeActionFromQValues()` ensures unseen actions (Q=0) are properly considered when all seen actions have negative Q-values.

### Q6: Approximate Q-Learning (4 points)
**File:** `qlearningAgents.py` - `ApproximateQAgent` class

Implements approximate Q-learning with feature extraction:
- **`getQValue(state, action)`** - Q(s,a) = w · f(s,a) (dot product)
- **`update(state, action, nextState, reward)`** - Updates weights using feature-based rule

**Weight Update:**
```
w_i ← w_i + α·difference·f_i(s,a)
where difference = (r + γ·max_{a'} Q(s',a')) - Q(s,a)
```

**Feature Extractors:**
- `IdentityExtractor` - One feature per (state, action) pair
- `SimpleExtractor` - Hand-crafted features for Pacman

**Benefits:**
- Generalizes across similar states
- Works on larger grids where tabular Q-learning fails

---

## Key Algorithms

### Value Iteration
1. Initialize V(s) = 0 for all states
2. For k iterations:
   - For each state s:
     - V_{k+1}(s) = max_a Σ_{s'} T(s,a,s') [R(s,a,s') + γV_k(s')]
3. Policy: π(s) = argmax_a Q(s,a)

### Q-Learning
1. Initialize Q(s,a) = 0 for all state-action pairs
2. For each step:
   - Observe (s, a, r, s')
   - Update: Q(s,a) ← Q(s,a) + α[r + γ·max_{a'} Q(s',a') - Q(s,a)]
   - Choose action using epsilon-greedy policy

### Epsilon-Greedy
- With probability ε: explore (random action)
- With probability 1-ε: exploit (best action)

Balances exploration vs exploitation.

---

## Implementation Details

### Value Iteration (Q1)
- Uses **batch updates**: all V_{k+1} values computed from V_k before updating
- Terminal states have value 0
- Handles states with no actions gracefully

### Q-Learning (Q3, Q5)
- Uses `util.Counter` for Q-value storage (defaults to 0.0 for unseen pairs)
- Random tie-breaking ensures proper exploration
- Terminal states: `computeValueFromQValues()` returns 0.0

### Random Tie-Breaking
Critical for proper exploration, especially in early training:
```python
# Find all actions with maximum Q-value
bestActions = [action for action in legalActions 
               if self.getQValue(state, action) == maxQ]
# Randomly choose among them
return random.choice(bestActions)
```

---

## Testing

### Test Structure
Each question has multiple test cases in `test_cases/qN/`:
- `.test` files define test parameters
- `.solution` files contain expected outputs

### Running Tests
- **All questions:** `python autograder.py`
- **One question:** `python autograder.py -q qN`
- **One test:** `python autograder.py -t test_cases/qN/test-name`

---

## Project Status

### ✅ Completed
- Q1: Value Iteration
- Q2: Policy Analysis
- Q3: Q-Learning
- Q4: Epsilon Greedy
- Q5: Q-Learning and Pacman

### ⏳ In Progress
- Q6: Approximate Q-Learning

---

## References

- **Course:** CS 471 - Artificial Intelligence (University of Oregon, Fall 2025)
- **Project:** Based on UC Berkeley CS188 Project 3
- **Project Description:** [CS 471 Project 3](https://classes.cs.uoregon.edu/25F/cs471/programming-projects/project3.html)

---

## Notes

- All Q-values default to 0.0 for unseen state-action pairs
- Terminal states have no legal actions and return None for actions
- The autograder uses fixed random seeds for reproducibility
- Pacman training games run in quiet mode by default (no GUI)

---

## Submission

Submit the following files to Canvas:
- `valueIterationAgents.py`
- `qlearningAgents.py`
- `analysis.py`

**Do NOT** submit files in a zip file or directory.

