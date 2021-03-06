import os
from argparse import ArgumentParser

import requests


# Leetcode URLs
API_URL = 'https://leetcode.com/api/problems/algorithms/'
PROBLEMS_URL_BASE = 'https://leetcode.com/problems/'

# Leetcode difficulties
DIFFICULTY_MAP = {
    1: 'Easy',
    2: 'Medium',
    3: 'Hard'
}

# Local file paths
TOP_LEVEL_DIRECTORY = os.path.dirname(os.path.abspath(__file__)) + '/..'
SOLUTION_PATH_BASE = '/leetcode/solutions/'

def main(slug: str) -> None:
    
    # Fetch all problem data
    r = requests.get(API_URL)
    r.raise_for_status()
    problem_data = r.json()

    # Find the problem corresponding to the given slug
    problems = problem_data['stat_status_pairs']
    problem = next((p for p in problems if p['stat']['question__title_slug'] == slug), None)

    # Extract relevant problem data
    id_ = problem['stat']['frontend_question_id']
    title = problem['stat']['question__title']
    difficulty = DIFFICULTY_MAP[problem['difficulty']['level']]
    link = PROBLEMS_URL_BASE + slug
    solution_path = SOLUTION_PATH_BASE + f"{id_}.py"
    
    # Add a row to the README table with problem data
    with open(TOP_LEVEL_DIRECTORY + '/leetcode/README.md', 'a') as f:
        f.write(f"| {id_} | [{title}]({link}) | [{id_}.py]({solution_path}) | {difficulty} |\n")

    # Add a file for the problem under solutions
    open(TOP_LEVEL_DIRECTORY + solution_path, 'w')


if __name__ == '__main__':

    # Command line arguments
    a = ArgumentParser()
    a.add_argument('--slug', '-s', required=True, help='URL slug of Leetcode problem to fetch. Ex: find-latest-group-of-size-m')
    args = a.parse_args()

    # Strip any '/' if applicable
    slug = args.slug.strip('/')

    # Execute main
    main(slug)
