import pandas as pd
import numpy as np

""" Creates a bigger iris data set. Randomizes the features in a class of iris.
    Interesting to see how this will train a model compared to the original data
    set.  Could use the original data set as the test data. 
    
    You will need the iris data file."""

#Optional
np.random.seed(23)

def create_arrays():
    file = '/home/filepath/Iris.csv'
    df = pd.read_csv(file)
    df_setosa = df[(df.Species == 'Iris-setosa')]
    df_versicolor = df[(df.Species == 'Iris-versicolor')]
    df_virginica = df[(df.Species == 'Iris-virginica')]
    return df_setosa, df_versicolor, df_virginica

def example_data(df, num, y):
    """ Repeat the features and mix them up."""
    sepal_length = np.array(df.iloc[:,1])
    sepal_length = np.repeat(sepal_length, num)
    sepal_length = random_data(sepal_length)

    sepal_width = np.array(df.iloc[:,2])
    sepal_width = np.repeat(sepal_width, num)
    sepal_width = random_data(sepal_width)

    petal_length = np.array(df.iloc[:,3])
    petal_length = np.repeat(petal_length, num)
    petal_length = random_data(petal_length)

    petal_width = np.array(df.iloc[:,4])
    petal_width = np.repeat(petal_width, num)
    petal_width = random_data(petal_width)

    num_examples = sepal_length.shape[0]

    species = np.full((num_examples,1), y, dtype=int)

    return np.column_stack((sepal_length, sepal_width, petal_length, petal_width, species))

def random_data(data):
    """Uses Pandas function to randomly shuffled data and
       return a numpy array."""
    df = pd.DataFrame(data)
    df = df.sample(frac=1)  #.reset_index(drop=True)
    return np.array(df)

def write_new_data(data_set):
    """ Function to write numpy array to csv if desired."""
    df = pd.DataFrame(data_set)
    df.columns = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm', 'Species']
    df.to_csv('/home/filepath/new_iris.csv', index=False)

df_setosa, df_versicolor, df_virginica = create_arrays()

setosa_data = example_data(df_setosa, 200, 1)
versicolor_data = example_data(df_versicolor, 200, 2)
virginica_data = example_data(df_virginica, 200, 3)

data_set = np.concatenate((setosa_data, versicolor_data, virginica_data), axis=0)

data_set = random_data(data_set)
write_new_data(data_set)
print(data_set)
