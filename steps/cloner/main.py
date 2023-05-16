import csv
import os

from git import Repo, GitCommandError
from tqdm import tqdm

import constants

def map_repo_name(name):
    if name[-1] == '/':
        name = name[:-1]
    return name.replace('/', '_')

def is_valid_row(number: str):
    return int(number) > 0


def iac_repos(target_csv_path: str, language: str):
    os.chdir('../')
    downloaded_repos = 0
    target_output_dir = f"{constants.REPOS_DIR}/{language}"
    if not os.path.exists(constants.REPOS_DIR):
        os.makedirs(target_output_dir)

    current_repos = set(target_output_dir)
    with open(target_csv_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            current_repos.add(row[0])

    print('Current repos:', len(current_repos))
    start_from = 0
    with open('count.txt', 'w') as downloaded_count:
        counter = 0
        for repo_name in tqdm(current_repos):
            counter += 1
            if counter < start_from:
                continue
            try:
                parts = repo_name.split('/')
                repo_path = os.path.join(target_output_dir, parts[-1])
                repo_url = repo_name
                repo = Repo.clone_from(repo_url, repo_path)
                downloaded_repos += 1
                downloaded_count.write(f'{downloaded_repos}: {repo_url}\n')
                downloaded_count.flush()
            except GitCommandError as e2:
                downloaded_count.write(f"{repo_name}\n")
                downloaded_count.flush()
                pass
            except Exception as e:
                    print('Unknown exception:', e)
    print('Downloaded repos:', downloaded_repos)

def main():
    for language in constants.LANGUAGES:
        print("Downloading repos for ", language)
        iac_repos(f"{constants.INPUT_REPOS_DIR}/{language}-repos.csv", language)

main()

