import os
import constants
from factory.labeler_factory import LabelerFactory
from factory.labelers.labeler import Labeler

arch_styles = {
    "java": {},
    "python": {},
    "javascript": {},
    "go": {},
    "typescript": {}
}

def calculate_label(file_path: str):
    results = {}
    all_found_keys = []
    maxi_score = 0
    maxi_key = ''
    for arch_key in arch_styles:
        all_found = True
        score = 0
        for term in arch_styles[arch_key]:
            found = search_str(file_path, term)
            if found: score += 1
            all_found = all_found and found
        if all_found: all_found_keys.append(arch_key)
        results[arch_key] = score
        if maxi_score <= score: maxi_key = arch_key
    if len(all_found_keys) > 0:
        maxi_score = 0
        maxi_key = ''
        for key in all_found_keys:
            if len(arch_styles[key]) >= maxi_score:
                maxi_key = key
    return results, all_found_keys, maxi_key

def main():
    for language in arch_styles:
        output_folder = f"{constants.labels_output}"
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        repos_path = f"{constants.repos_dir}/{language}"
        factory = LabelerFactory()
        labeler = factory.create_labeler(language)
        add_labels_by_functions(repos_path, language, labeler)

def add_labels_by_functions(repos_path, language, labeler: Labeler):
    if not os.path.exists(repos_path):
        return
    current_repos = set(os.listdir(repos_path))
    for repo_name in current_repos:
        print(repos_path, repo_name)
        for dirpath, dir, files in os.walk(f'{repos_path}/{repo_name}'):
            for file in files:
                labeler.get_label(dirpath, file, language)

def add_labels_by_repo(current_repos):
    for repo_name in current_repos:
        results = {key: 0 for key in arch_styles}
        for dirpath, dir, files in os.walk(f'repos/{repo_name}'):
            for file in files:
                if file.endswith(".java"):
                    file_path = os.path.join(dirpath, file)
                    res, all_found, max_key = calculate_label(file_path)
                    for key in arch_styles:
                        results[key] += res[key]
        maxi_k, maxi_v = '', 0
        for key in results:
            if results[key] >= maxi_v:
                maxi_k = key
                maxi_v = results[key]
        if maxi_v == 0:
            maxi_k = 'unlabeled'
        save_label(repo_name, maxi_k)
def save_label(filepath, label):
    with open(constants.labels_output, 'a') as labels:
        print("saving", label, filepath)
        labels.write(f'{label},{filepath}\n')
        labels.flush()
        # check if string present in a file
def search_str(file_path, word):
        with open(file_path, 'r') as file:
            # read all content of a file
            try:
                content = file.read()
                if word in content:
                    return True
                else:
                    return False
            except Exception as e:
                print("error reading file", file, e)
                return False


main()
