import seaborn as sns


def read_dataset():
    return sns.load_dataset('tips').sample(100)