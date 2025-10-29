# CS 471/571 – Introduction to Artificial Intelligence  
## Project 2: Multi-Agent Search (Fall 2025)

**Due:** November 5, 2025, at 11:59 PM  
**Course:** CS 471/571 – Introduction to Artificial Intelligence  
**Instructor:** University of Oregon  

---

## Overview

In this project, you will implement multi-agent search algorithms for the classic Pacman environment.  
You will design agents that can reason about adversarial and stochastic opponents (ghosts),  
and build progressively stronger AI decision systems using Reflex, Minimax, Alpha-Beta, and Expectimax logic.

The project culminates with designing a custom evaluation function to balance offensive and defensive play.

---

## Project Files

### Files You’ll Edit
- `multiAgents.py` — All of your multi-agent search agents and evaluation functions.

### Files You’ll Reference
- `pacman.py` — Main entry point for the game and GameState definitions.  
- `game.py` — Core game logic for Pacman and Ghost agents.  
- `util.py` — Useful data structures and helper functions (e.g., stacks, queues).

### Supporting Files (Read Only)
- `graphicsDisplay.py`, `graphicsUtils.py`, `textDisplay.py` — Visual display components.  
- `ghostAgents.py` — Predefined ghost agent behaviors.  
- `keyboardAgents.py` — Human-controlled Pacman agent.  
- `layout.py` — Parses and stores map layouts.  
- `autograder.py`, `testParser.py`, `testClasses.py`, `multiagentTestClasses.py` — Autograding tools and tests.  
- `test_cases/` — Directory of individual test scenarios for each question.

Do not modify any files other than `multiAgents.py`.

---

## Running and Testing

You can test your code using:

```bash
python autograder.py
```

Run a specific question:

```bash
python autograder.py -q q2
```
Control graphics:
- graphics → Forces GUI mode
- no-graphics → Runs without graphics

Run multiple games in sequence:
```bash
python pacman.py -p ReflexAgent -n 10 --no-graphics
```
---
## Q1. Reflex Agent (4 points)

**Goal:** Improve `ReflexAgent` to make intelligent, reactive moves.  

Your agent should:
- Consider both food and ghost distances.
- Use the reciprocal of distances for smoother scoring.
- Handle multiple ghosts and varied layouts.

Run and test:
```bash
python autograder.py -q q1
python autograder.py -q q1 --no-graphics
```
---
## Q2. Minimax Agent (5 points)

**Goal:** Implement a full minimax search in `MinimaxAgent`.

Requirements:
- Handle multiple ghosts (multiple min layers per max layer).
- Depth `d` corresponds to `d` full cycles of (Pacman + all ghosts).
- Use `self.depth` and `self.evaluationFunction` for configuration.

Run and test:
```bash
python autograder.py -q q2
python pacman.py -p MinimaxAgent -l minimaxClassic -a depth=4
```

---
## Q3. Alpha-Beta Pruning (5 points)

**Goal:** Optimize Minimax using alpha-beta pruning in `AlphaBetaAgent`.

Requirements:
- Must match Minimax’s minimax values exactly.
- Do not reorder children — process in `getLegalActions()` order.
- Do not prune on equality (to match autograder logic).

Run and test:
```bash
python autograder.py -q q3
python pacman.py -p AlphaBetaAgent -a depth=3 -l smallClassic
```

## Q4. Expectimax (5 points)

**Goal:** Implement the `ExpectimaxAgent` in `multiAgents.py` to handle stochastic (non-deterministic) ghost behavior.  
Unlike Minimax or Alpha-Beta agents that assume perfectly rational adversaries, the Expectimax agent models **ghosts as random agents** that act according to a uniform probability distribution.

---

### Requirements
- Replace minimizer nodes in your tree with **expectation nodes** that compute the **average utility** over all legal ghost actions.  
- Assume each ghost chooses randomly and uniformly among its legal moves.
- Pacman remains the **maximizer**, but ghosts are now **chance nodes**.
- Depth values still correspond to full rounds of moves (Pacman + all ghosts).
- Use `self.depth` and `self.evaluationFunction` appropriately for configuration.

---

### Implementation Notes
- Reuse the recursive structure from your Minimax implementation, modifying it to compute expected values for ghost turns.
- Expectimax does **not prune branches**, since all outcomes contribute to the expected value.
- For multiple ghosts, handle each ghost index sequentially (as in Minimax).
- When computing expectations, weight all legal actions equally.
---
## Q5. Evaluation Function (6 points)

**Goal:** Design a superior evaluation function in `betterEvaluationFunction`.

Requirements:
- Evaluate states (not state-action pairs).
- Incorporate features like:
  - Distance to food
  - Ghost proximity
  - Power pellets
  - Remaining capsules
  - Game score

**Performance Criteria (Depth 2 Search):**
- Must win > 50% of games on `smallClassic` with one random ghost.
- Should achieve ~1000 average score when winning.

**Grading Breakdown:**
| Condition | Points |
|------------|---------|
| Wins ≥ 1 game | +1 |
| Wins ≥ 5 games | +1 |
| Wins 10/10 | +2 |
| Avg. score ≥ 500 | +1 |
| Avg. score ≥ 1000 | +2 |
| Average runtime < 30s | +1 |

Run and test:
```bash
python autograder.py -q q5
python autograder.py -q q5 --no-graphics