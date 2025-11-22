import os
import random
import re

# Constants
DAMPING = 0.85  # Damping factor for PageRank
SAMPLES = 10000  # Number of samples for PageRank sampling

# Main function
def main():
    # User input for directory containing HTML pages
    directory = input("Enter the directory path containing HTML pages: ")
    directory = directory.strip('"')
    
    # Crawling the directory to extract links and create a corpus
    corpus = crawl(directory)
    
    # Printing the corpus (for debugging purposes)
    print(corpus)
    
    # Calculating PageRank using sampling method
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    
    # Calculating PageRank using iterative method
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")

# Function to crawl directory and extract links from HTML pages
def crawl(directory):
    pages = {}
    for filename in os.listdir(directory):
        if filename.endswith(".html"):
            with open(os.path.join(directory, filename), 'r') as f:
                contents = f.read()
                # Extract links using regular expressions
                links = re.findall(r"<a\s+(?:[^>]*)href=\"([^\"]*)\"", contents)
                # Removing self-links and adding to pages dictionary
                links = [link for link in links if link != filename]
                pages[filename] = set(links)
    return pages

# Function to generate the transition model for a given page
def transition_model(corpus, page, damping_factor):
    model = {}
    linked_pages = corpus[page]
    num_linked_pages = len(linked_pages)
    if num_linked_pages == 0:
        return {p: 1 / len(corpus) for p in corpus}

    prob_linked = damping_factor / num_linked_pages
    prob_random = (1 - damping_factor) / len(corpus)

    for p in corpus:
        model[p] = prob_random
    for p in linked_pages:
        model[p] += prob_linked
    return model

# Function to calculate PageRank using random sampling
def sample_pagerank(corpus, damping_factor, n):
    sample_count = {page: 0 for page in corpus}
    current_page = random.choice(list(corpus.keys()))
    for _ in range(n):
        sample_count[current_page] += 1
        model = transition_model(corpus, current_page, damping_factor)
        current_page = random.choices(list(model.keys()), weights=model.values(), k=1)[0]
    pagerank = {page: count / n for page, count in sample_count.items()}
    return pagerank

# Function to calculate PageRank using iterative method
def iterate_pagerank(corpus, damping_factor, epsilon=0.001):
    N = len(corpus)  # Total number of pages
    initial_rank = 1 / N  # Initial rank for each page
    ranks = {page: initial_rank for page in corpus}  # Initial rank for each page

    while True:
        new_ranks = {}  # Dictionary to store new ranks for each page
        max_diff = 0  # Maximum difference in rank for convergence detection

        for page in corpus:
            new_rank = (1 - damping_factor) / N  # Initialize new rank for the page
            
            # Calculate new rank based on incoming links from other pages
            for incoming_page, links in corpus.items():
                if page in links:
                    num_links = len(links)
                    new_rank += damping_factor * (ranks[incoming_page] / num_links)
            
            new_ranks[page] = new_rank  # Store new rank for the page

            # Update maximum difference for convergence detection
            max_diff = max(max_diff, abs(new_rank - ranks[page]))

        ranks = new_ranks  # Update ranks with new ranks

        # Check for convergence
        if max_diff < epsilon:
            break

    return ranks

# Entry point of the script
if __name__ == "__main__":
    main()
