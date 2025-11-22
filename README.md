# PageRank Algorithm Implementation

## Overview

This project implements the PageRank algorithm using two different approaches: random sampling and iterative calculation. The implementation analyzes web page importance based on their link structure within a corpus of HTML pages.

## Project Structure

The implementation consists of:
- Main Python script (pagerank.py) containing the PageRank algorithms
- Three test corpora (corpus0, corpus1, corpus2) with interconnected HTML pages
- Each corpus represents a different web page network for testing

## Implementation Details

### Core Algorithm Components

**Markov Chain Foundation**
The implementation treats web page navigation as a Markov Chain, where the probability of visiting a page depends only on the current page, not the browsing history. Each page represents a state, and hyperlinks define transition probabilities between states.

**Damping Factor**
Used a damping factor of 0.85, meaning:
- 85% probability: user follows a link from the current page
- 15% probability: user jumps to any random page in the corpus

### Method 1: Random Sampling Approach

Implemented a Monte Carlo simulation that:
- Starts from a randomly selected page
- Performs 10,000 iterations of random page visits
- Tracks visit frequency for each page
- Calculates PageRank as the proportion of visits to each page

Key implementation steps:
1. Initialize sample count dictionary for all pages
2. Select initial page randomly
3. For each iteration, update visit count and determine next page using transition probabilities
4. Normalize counts to obtain final PageRank values

### Method 2: Iterative Calculation Approach

Implemented the mathematical PageRank formula iteratively:
- Started with equal initial ranks (1/N for N pages)
- Applied the PageRank formula: PR(p) = (1-d)/N + d * sum(PR(i)/NumLinks(i))
- Repeated until convergence (changes less than 0.001)

Key implementation aspects:
1. Handled pages with no outgoing links by treating them as linking to all pages
2. Calculated incoming link contributions for each page
3. Iterated until maximum rank change fell below epsilon threshold

### Supporting Functions

**crawl(directory)**
Parses HTML files in the specified directory and extracts hyperlinks using regular expressions. Returns a dictionary mapping each page to its set of outgoing links.

**transition_model(corpus, page, damping_factor)**
Calculates the probability distribution for the next page visit given:
- Current page location
- Available links from that page
- Random jump probability

## Test Corpora

### Corpus 0
Simple 4-page network (1.html through 4.html) with linear link structure for basic algorithm verification.

### Corpus 1
AI-related topics network including pages about search algorithms (BFS, DFS), game theory (Minimax), and game implementations (TicTacToe, Minesweeper).

### Corpus 2
Computer science topics including programming languages (C), algorithms, recursion, logic, and AI concepts.

## Results and Observations

Both sampling and iterative methods produce similar PageRank values, validating the implementation. Pages with more incoming links from important pages receive higher ranks.

The iterative method converges efficiently, typically within a few dozen iterations. The sampling method provides good approximations with 10,000 samples.

## Technical Challenges Addressed

1. Ensuring proper convergence in the iterative algorithm through epsilon threshold checking
2. Correctly implementing the PageRank mathematical formula with proper summation over incoming links
3. Handling edge cases such as pages with no outgoing links
4. Maintaining numerical stability and ensuring rank values sum to 1.0

## Practical Applications

This implementation demonstrates how search engines evaluate web page importance beyond simple keyword matching. The algorithm considers the network structure of interconnected pages, rewarding pages that are referenced by other authoritative sources.

## Dependencies

- Python standard library (os, random, re)
- No external packages required

## Usage

Run the program by providing a directory containing HTML pages:

```
python pagerank.py
Enter the directory path containing HTML pages: /path/to/corpus
```

The program outputs PageRank results from both sampling and iteration methods, allowing comparison of the two approaches.
