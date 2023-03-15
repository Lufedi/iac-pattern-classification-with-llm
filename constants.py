

REPO_DIR = '/Users/lfeliped/pipe/master/experiments/An-analysis-of-diagram-images-on-Git-repositories'
LABELS_FILE = '/Users/lfeliped/pipe/master/experiments/An-analysis-of-diagram-images-on-Git-repositories/labeling/labels.txt'
TRAIN_FOLDER = '/Users/lfeliped/temp/pipeline'
DATASET = 'my_dataset'


CODE2VEC_DIR = '/Users/lfeliped/pipe/master/premodels/code2vec'


TRAIN_DIRS = ['train', 'test', 'val']

models = {
    "code2vec": {
        "dir": CODE2VEC_DIR
    },
    "code2seq": {
        "dir": '/Users/lfeliped/pipe/master/premodels/code2seq'
    }
}
