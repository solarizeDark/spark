import os
from dataset_loader import *
from kNN import *

features = {}
answers = {}

answers_file = open('E:\\stud\\spark\\author_book\\book_names.txt', 'r')
lines = answers_file.readlines()
for line in lines:
    answers[line[line.find(' ') + 1 : line.rfind(' ')]] = int(line[line.rfind(' ') + 1 : -1])


for file in os.listdir('E:\\stud\\spark\\features'):
    features[file[:file.rfind('.')]] = load_dataset_column_as_row('E:\\stud\\spark\\features\\' + file)

dataset = []
for name in features.keys():
    answer = answers[name[:name.rfind('_')]]
    dataset.append([features[name], answer])

mean_accuracy = kNN_algorithm_mean_accuracy_books_analyzing(dataset)

# folds = cross_validation_split(dataset)
# neighbors = get_neighbors_txt_analyzing(dataset[0], dataset, 10)
# ans = predict_classification_books_analyzing(dataset[0], dataset, 10)
# a = 5
