# CS 471: Introduction to Artificial Intelligence - Project 1 Task Plan

## Course & Project Overview

* **Course:** CS 471/571: Introduction to Artificial Intelligence (Fall 2025)
* **Instructor:** Thanh H. Nguyen
* **Project 1:** Search in Pac-Man
* **Objective:** This project involves applying graph search algorithms to help Pac-Man navigate mazes. You will implement uninformed search algorithms like Depth-First Search (DFS) and Breadth-First Search (BFS), as well as informed (heuristic) search algorithms like Uniform-Cost Search (UCS) and A* search.
* **Due Date:** October 22nd, 2025

---

## High-Level Objective

The goal is to implement several search algorithms that will solve different Pac-Man scenarios. The project is divided into four main questions, each requiring the implementation of a specific algorithm. A successful project will have a Pac-Man agent that can efficiently find paths, collect all dots, and find the cheapest path to collect dots.

## Team Roles & Responsibilities

* **Madeline L: Foundations & Uninformed Search**
    * Focuses on setting up the project environment and implementing the fundamental data structures and the first two search algorithms (DFS and BFS). This role lays the groundwork for the entire project.
* **Vikram T: Informed & Heuristic Search**
    * Focuses on implementing the more complex, cost-based search algorithms (UCS and A*) and is responsible for designing the crucial heuristic for the A* search portion.

---

## Detailed Task Breakdown

### **Part 0: Project Setup & Code Analysis (Both Partners)**

* **Task:** Download the project source code and familiarize yourselves with the existing files.
* **Key Files to Understand:**
    * `pacman.py`: The main file that runs the Pac-Man game. You'll use this to test your algorithms.
    * `search.py`: Where you will write all of your search algorithm implementations.
    * `searchAgents.py`: Contains the `SearchAgent` class that connects your algorithms to the Pac-Man world.
    * `game.py`: Defines the Pac-Man world logic (states, actions, etc.).
* **Action Item:** Ensure both partners can run the baseline game by executing `python pacman.py` in the terminal. Discuss how the different files interact, particularly how an `action` returned from `search.py` is used in the game.

### **Part 1: Uninformed Search**

#### **Question 1: Depth-First Search (DFS) - Madeline L**.

* **Objective:** Implement the DFS algorithm to find a path to a fixed dot in the maze.
* **File to Edit:** `search.py`
* **Function to Implement:** `depthFirstSearch`
* **Data Structure:** You will need a **Stack** for the fringe. The project provides a `util.Stack` class you can use.
* **Testing:** Run the following command to test your implementation:
    ```bash
    python pacman.py -l tinyMaze -p SearchAgent
    ```
* **Success Metric:** Pac-Man should successfully find the path in the `tinyMaze`.

#### **Question 2: Breadth-First Search (BFS) - Vikram T.**

* **Objective:** Implement the BFS algorithm. This is often used to find the shortest path in terms of the number of steps.
* **File to Edit:** `search.py`
* **Function to Implement:** `breadthFirstSearch`
* **Data Structure:** You will need a **Queue** for the fringe. Use the provided `util.Queue`.
* **Testing:** Run the following command:
    ```bash
    python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
    ```
* **Success Metric:** Pac-Man should find the optimal path in terms of path length.

### **Part 2: Informed Search & Heuristics**

#### **Question 3: Uniform-Cost Search (UCS) - Madeline L.**

* **Objective:** Implement the UCS algorithm to find the least-cost path. This differs from BFS when action costs are not uniform.
* **File to Edit:** `search.py`
* **Function to Implement:** `uniformCostSearch`
* **Data Structure:** You will need a **Priority Queue** for the fringe to handle path costs. Use `util.PriorityQueue`. The priority should be the cumulative cost of the path to a node.
* **Testing:** Run the following commands:
    ```bash
    python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
    python pacman.py -l mediumDottedMaze -p StayEastSearchAgent
    ```
* **Success Metric:** Pac-Man must find the path with the lowest total cost, which may not be the shortest in terms of steps.

#### **Question 4: A\* Search & Heuristics** - Vikram T.

* **Objective:** Implement the A\* search algorithm and design an effective heuristic.
* **File to Edit:** `search.py`
* **Functions to Implement:** `aStarSearch` and a non-trivial heuristic for the `FoodSearchProblem`.
* **Data Structure:** You will again use a **Priority Queue**. The priority for A\* is the sum of the path cost and the heuristic value: $g(n) + h(n)$.
* **Heuristic Design:** For the "eat all dots" problem (`FoodSearchProblem`), you will need to design an **admissible** and **consistent** heuristic. Think about what information you can use from the `SearchProblem` state to estimate the remaining cost. A good heuristic is crucial for performance.
* **Testing:**
    ```bash
    python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
    ```
* **Success Metric:** A\* should find the goal dot by expanding far fewer nodes than BFS, especially in large mazes.

---

## Integration and Final Submission

* **Code Merge:** After both partners have completed and tested their sections, merge the code into the final `search.py` file.
* **Final Review (Both Partners):**
    * Run all provided autograder tests to ensure all parts work together correctly.
    * Review the code for clarity, comments, and adherence to the project guidelines.
    * Make sure there are no hard-coded solutions and that your code is general enough for any maze layout.
* **Submission:**
    * Submit only the `search.py` and `searchAgents.py` files.
    * If you worked in a pair, ensure both partners' names and student IDs are included in the header of the files.
    * Follow the specific submission instructions provided on the course website or Canvas.