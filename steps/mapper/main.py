import os
import shutil
import random
import constants
import json

def read_labels(label_file):
    results = {}
    if not os.path.exists(label_file):
        return results
    with open(label_file) as f:
        lines = f.readlines()
        for line in lines:
            data = line.split(",")
            key = data[0]
            if key == "unlabaled": continue
            if not key in results:
                results[key] = []
            results[key].append(data[1])

    for key in results:
        print(f"{key}: {len(results[key])}")
    return results

def print_to_jsonl_file(files, out_file_name, label):
    for file in files:
        file_name =  file
        src = file_name.replace('\\', '/').replace('\n', '')
        try:
            with open(src) as f:
                content = f.read()
                out = { "code": content,  "label": label}
                json_object = json.dumps(out)
                with open(f"{constants.JSONL_OUTPUT_DIR}/{out_file_name}", "a") as out_file:
                    out_file.write(json_object + "\n")
        except Exception  as e:
            print(e)
            continue

def write_jsonl(files, label):
    random.shuffle(files)
    size_train = int(len(files) * 0.75)
    size_val = int(len(files) * 0.15)
    size_test = len(files) - size_train - size_val
    print(len(files), size_train, size_val, size_test)
    train_set = files[:size_train]
    val_set = files[size_train:size_train + size_val]
    test_set = files[size_train + size_val:]
    print(len(train_set), len(val_set), len(test_set))
    print_to_jsonl_file(train_set, "train.jsonl", label)
    print_to_jsonl_file(val_set, "valid.jsonl", label)
    print_to_jsonl_file(test_set, "test.jsonl", label)
def tunning():
    '''
    1. Read labels.csv files and split into test, val and train sets
    2. copy repos to train, test and validate folder
        1.1 decide randomlly the partitions
    3. Create jsonl files with the labels and the code
    '''
    if not os.path.exists(constants.JSONL_OUTPUT_DIR):
        os.makedirs(constants.JSONL_OUTPUT_DIR)
    for language in constants.LANGUAGES:
        print("Mapping:", language)
        file_path = f"{constants.LABELS_FILE}/{language}-labels.csv"
        map_archkey_to_files = read_labels(file_path)
        if "unlabeled" in map_archkey_to_files:
            # for file in map_archkey_to_files["unlabeled"]:
                # map_archkey_to_files["event-driven"].append(file)
            del map_archkey_to_files["unlabeled"]

        keys_n = list(map_archkey_to_files.keys())

        for i in range(len(keys_n)):
            arch_key = keys_n[i]
            # repos_location = f"{constants.REPO_DIR}/{language}"
            # copy_files_to_train_folders(repos_location, map_archkey_to_files[arch_key], constants.TRAIN_FOLDER)
            write_jsonl(map_archkey_to_files[arch_key], i)

def main():
    tunning()

main()
# add_labels_to_asts('piperules')

