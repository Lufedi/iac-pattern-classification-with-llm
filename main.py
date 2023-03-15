import os
import shutil
import random
import constants

def copy_files(files, source, target):
    if not os.path.exists(target):
        os.makedirs(target)
    for file in files:
        try:
            src = f"{source}/{file}"
            src = src.replace('\\', '/').replace('\n', '')
            f = file.replace('\\', '/').replace('\n', '').split('/')
            dst = f"{target}/{f[-1]}"
            shutil.copyfile(src, dst)
        except:
            continue

def copy_files_to_train_folders(repos_dir: str, files, train_folder: str):
    random.shuffle(files)
    size_train = int(len(files) * 0.75)
    size_val = int(len(files) * 0.15)
    size_test = len(files) - size_train - size_val
    print(len(files), size_train, size_val, size_test)
    train_set = files[:size_train]
    val_set = files[size_train:size_train + size_val]
    test_set = files[size_train + size_val:]
    print(len(train_set), len(val_set), len(test_set))
    copy_files(train_set, repos_dir, f"{train_folder}/train/files")
    copy_files(val_set, repos_dir, f"{train_folder}/val/files")
    copy_files(test_set, repos_dir, f"{train_folder}/test/files")

def read_labels(label_file):
    results = {}
    with open(label_file) as f:
        lines = f.readlines()
        for line in lines:
            data = line.split(",")
            key = data[0]
            if not key in results:
                results[key] = []
            results[key].append(data[1])
    return results

def remove_pipeline_data():
    for dir in constants.TRAIN_DIRS:
        shutil.rmtree(f"{constants.TRAIN_FOLDER}/{dir}")

def generate_ast_files():
    os.system('cd /users/lfeliped/pipe/master/premodels/code2vec/ && sh /users/lfeliped/pipe/master/premodels/code2vec/preprocess.sh ast')

def generate_model_files():
    os.system('cd /users/lfeliped/pipe/master/premodels/code2vec/ && sudo sh /users/lfeliped/pipe/master/premodels/code2vec/preprocess.sh')

def train_model():
    os.system('cd /users/lfeliped/pipe/master/premodels/code2vec/ && sudo sh /users/lfeliped/pipe/master/premodels/code2vec/train.sh')
def add_labels_to_asts(label):
    for train_file_name in constants.TRAIN_DIRS:
        file_name = f"{constants.CODE2VEC_DIR}/{constants.DATASET}.{train_file_name}.raw.txt"
        with open(file_name, 'r') as file:
            lines = file.readlines()
            new_lines = []
            for line in lines:
                data = line.split(" ")
                data[0] = label
                ll = str.join(" ", data)
                new_lines.append(ll)
        string_to_write = str.join("", new_lines)
        file_name = f"{constants.CODE2VEC_DIR}/{constants.DATASET}.{train_file_name}.raw.txt:{label}"
        with open(file_name, "w") as new_file:
            new_file.write(string_to_write)

def merge_files(labels):
    for train_file_name in constants.TRAIN_DIRS:
        file_name_prefix = f"{constants.CODE2VEC_DIR}/{constants.DATASET}.{train_file_name}.raw.txt"
        with open(file_name_prefix, 'wb') as ffi:
            for label in labels:
                ffi.write(b"\n")
                with open(f"{file_name_prefix}:{label}", 'rb') as labeled_file:
                    shutil.copyfileobj(labeled_file, ffi)

def remove_temporary_label_files(labels):
    for train_file_name in constants.TRAIN_DIRS:
        for label in labels:
            file_name = f"{constants.CODE2VEC_DIR}/{constants.DATASET}.{train_file_name}.raw.txt:{label}"
            os.remove(file_name)


def main():

    '''
    1. copy repos to train, test and validate folder
        1.1 decide randomlly the partitions
    2. run preprocessor until AST path generation
    3. modify tags witht the architecture styles
    4. run preprocessor.py(need sudo)
    5. train the model
    6. test the model
    '''


    map_archkey_to_files = read_labels(constants.LABELS_FILE)
    if "unlabeled" in map_archkey_to_files:
        del map_archkey_to_files["unlabeled"]
    for arch_key in map_archkey_to_files:
        print("Generating files for", arch_key)
        copy_files_to_train_folders(constants.REPO_DIR, map_archkey_to_files[arch_key], constants.TRAIN_FOLDER)
        generate_ast_files()
        break
        # add_labels_to_asts(arch_key)
    # merge_files(map_archkey_to_files.keys())
    generate_model_files()
    # remove_temporary_label_files(map_archkey_to_files.keys())
    remove_pipeline_data()
main()
# add_labels_to_asts('piperules')

