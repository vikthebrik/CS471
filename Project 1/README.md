# Project 1 — Search (Pacman)

**Course:** CS 471/571 — Introduction to Artificial Intelligence, Fall 2025  
**Due:** **Wed, Oct 22 at 11:59 pm**

## Overview
In this project you’ll implement general search algorithms (DFS, BFS, UCS, A*) and design heuristics to guide Pacman through mazes and food-collection tasks. You’ll develop in `search.py` and `searchAgents.py`, then validate with the provided autograder.

---

## Repository / File Breakdown
**Files you will edit (and submit):**
- `search.py` — core search algorithms (DFS, BFS, UCS, A*).
- `searchAgents.py` — search-based agents, state representations, and heuristics.

**Files you may read/use:**
- `pacman.py` — runs games; defines `GameState`.
- `game.py` — core game logic and helper types.
- `util.py` — data structures (`Stack`, `Queue`, `PriorityQueue`).

**Supporting files (no edits needed):**
- `graphicsDisplay.py`, `graphicsUtils.py`, `textDisplay.py`, `ghostAgents.py`, `keyboardAgents.py`, `layout.py`, `autograder.py`, `testParser.py`, `testClasses.py`, `searchTestClasses.py`, and `test_cases/`.

**Submission:** Upload **only** `search.py` and `searchAgents.py` to Canvas (no zip). If you worked with a partner, list them.

**Academic Honesty:** Code will be compared across submissions; submit your own work.

---

## Setup & Running
- Play Pacman: `python pacman.py`  
- Options/help: `python pacman.py -h`  
- Run autograder for a question (examples): `python autograder.py -q q1` • `-q q2` • … • `-q q8`

---

## Questions, Requirements, & Commands
> Return **legal action lists** and use the provided `util.py` data structures. Graph-search versions should avoid revisiting explored states.

### Q1 — Depth-First Search (3 pts)
Implement `depthFirstSearch` in `search.py`.
```
python pacman.py -l tinyMaze -p SearchAgent
python pacman.py -l mediumMaze -p SearchAgent
python pacman.py -l bigMaze -z .5 -p SearchAgent
```
Autograder: `python autograder.py -q q1`

### Q2 — Breadth-First Search (3 pts)
Implement `breadthFirstSearch` in `search.py`.
```
python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5
```
Autograder: `python autograder.py -q q2`

### Q3 — Uniform-Cost Search (3 pts)
Implement `uniformCostSearch` in `search.py`.
```
python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
python pacman.py -l mediumDottedMaze -p StayEastSearchAgent
python pacman.py -l mediumScaryMaze -p StayWestSearchAgent
```
Autograder: `python autograder.py -q q3`

### Q4 — A* Search (3 pts)
Implement `aStarSearch` in `search.py`.
```
python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
```
Autograder: `python autograder.py -q q4`

### Q5 — Corners Problem: Representation (3 pts)
Implement `CornersProblem` in `searchAgents.py`.
```
python pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
```
Autograder: `python autograder.py -q q5`

### Q6 — Corners Heuristic (3 pts)
Implement `cornersHeuristic` in `searchAgents.py`.
```
python pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5
```
Autograder: `python autograder.py -q q6`

### Q7 — Eating All the Dots Heuristic (4 pts, + up to 1 extra)
Implement `foodHeuristic` in `searchAgents.py`.
```
python pacman.py -l testSearch -p AStarFoodSearchAgent
python pacman.py -l trickySearch -p AStarFoodSearchAgent
```
Autograder: `python autograder.py -q q7`

### Q8 — Suboptimal (Greedy) Closest-Dot (3 pts)
Implement `findPathToClosestDot` in `searchAgents.py`.
```
python pacman.py -l bigSearch -p ClosestDotSearchAgent -z .5
```
Autograder: `python autograder.py -q q8`

---

## Work Split (Pair Programming)
Assigning **odd**–numbered questions to **Madeline L.** and **even**–numbered to **Vikram T.**:

| Question | Topic | Assigned To |
|-----------|--------|--------------|
| Q1 | Depth-First Search | **Madeline L.** |
| Q2 | Breadth-First Search | **Vikram T.** |
| Q3 | Uniform-Cost Search | **Madeline L.** |
| Q4 | A* Search | **Vikram T.** |
| Q5 | Corners Problem: Representation | **Madeline L.** |
| Q6 | Corners Heuristic | **Vikram T.** |
| Q7 | Eating All the Dots: Heuristic | **Madeline L.** |
| Q8 | Suboptimal Search (Closest-Dot) | **Vikram T.** |

**Collaboration plan:**  
- Share utility helpers but keep algorithm/heuristic code authored by the assigned person.  
- Cross-review each PR and run `autograder.py -q qi` before merging.

---

## Tips & Gotchas
- Always return a **list of legal actions** from your search routines.  
- Use **Stack**, **Queue**, and **PriorityQueue** from `util.py`.  
- Implement **graph-search** (track explored states).  
- Use `--frameTime 0` for speed; `-z .5` for zoom.

---

## How to Submit
Upload `search.py` and `searchAgents.py` only to Canvas. Add partner info to the submission.

## Credits
Assignment adapted from the UC Berkeley Pacman projects.
