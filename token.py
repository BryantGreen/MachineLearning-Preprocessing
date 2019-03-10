
import tensorflow as tf

file =  'gen1' # Sample text file   
txt = open(file).read()
# Create a word list
txt = txt.split()

print(txt) #test
    
tokenizer = tf.keras.preprocessing.text.Tokenizer(num_words=1000)        
tokenizer.fit_on_texts(txt)
print(tokenizer)

sequences = tokenizer.texts_to_sequences(txt)

one_hot_results = tokenizer.texts_to_matrix(txt, mode='binary')

word_index = tokenizer.word_index
print(word_index)
print('%s Number of unique tokens ' % len(word_index))