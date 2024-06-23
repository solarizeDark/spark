Model for determination in wich century book was written.
I`ve taken 20 russian authors 19 and 20 centuries, 10 for
each century. Initial data - 1155 books.

Dataset
For each book counted mappings "word-amount of this word in book"
Words length less then 5 letters goes out. 
Features for book - map with top 20 by amount words with no suffixes.

I used kNN with weights. Weight - amount of occurence. Evaluated with
cross validation, with 5 folds. Result: mse - 0.69
