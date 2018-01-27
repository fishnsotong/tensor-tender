import pandas as pd
import tensorflow as tf

TRAIN_URL = '/data/trainingData.csv'
TEST_URL = "/data/testData.csv"

CSV_COLUMN_NAMES = ["Alcoholic beverage", "Animal product", "cereal/crop", "Dairy",
"fish/seafood", "Flower", "Fruit", "Herb", "Meat", "Nut/seed", "Plant", "Plant derivative",
"Spice", "Vegetable", "Coke", "Sprite", "Orange Fanta", "Lemonade", "Apple Juice"]

def load_data(label_names = ["Coke", "Sprite", "Orange Fanta", "Lemonade", "Apple Juice"]): #include all other labels afterwards
    """Parses the csv file in TRAIN_URL and TEST_URL."""

    # Create a local copy of the training set.
    train_path = tf.keras.utils.get_file(fname=TRAIN_URL.split('/')[-1],
                                         origin=TRAIN_URL)
    # train_path now holds the pathname: ~/.keras/datasets/iris_training.csv

    # Parse the local CSV file.
    train = pd.read_csv(filepath_or_buffer = train_path,
                        names=CSV_COLUMN_NAMES,  # list of column names
                        header=0  # ignore the first row of the CSV file.
                       )
    # train now holds a pandas DataFrame, which is data structure
    # analogous to a table.

    # 1. Assign the DataFrame's labels (the right-most column) to train_label.
    # 2. Delete (pop) the labels from the DataFrame.
    # 3. Assign the remainder of the DataFrame to train_features
    train_features = [];
    train_labels = [];
    for i in train:
        train_features[i] = train[i]
        train_labels[i] = train[i]
    del train_features[-5:]
    del train_labels[:-5]

    test_path = tf.keras.utils.get_file(TEST_URL.split('/')[-1], TEST_URL)
    test = pd.read_csv(test_path, names=CSV_COLUMN_NAMES, header=0)
    test_features = [];
    test_labels = [];
    for i in test:
        test_features[i] = train[i]
        test_labels[i] = train[i]
    del test_features[-5:]
    del test_labels[:-5]

     # Return four DataFrames.
    return (train_features, train_label), (test_features, test_label)


def maybe_download():
    train_path = tf.keras.utils.get_file(TRAIN_URL.split('/')[-1], TRAIN_URL)
    test_path = tf.keras.utils.get_file(TEST_URL.split('/')[-1], TEST_URL)

    return train_path, test_path
