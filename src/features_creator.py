import os
import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split, regexp_replace, lower, col, length, substring
from pyspark.sql.types import StringType

spark = SparkSession.builder.getOrCreate()

for title in os.listdir('E:\\stud\\spark\\books'):
    textFile = spark.read.text('E:\\stud\\spark\\books\\' + title)

    # deleting rows with page counting
    textFile = textFile.withColumn('value', regexp_replace('value', r'^[-+]?[0-9]+$', ''))
    textFile = textFile.filter(textFile.value != '')

    word_amounts = textFile.select(lower(col('value')).alias('words'))
    word_amounts = word_amounts.withColumn('words', regexp_replace('words', r'[(){}/!–.,?:;"»<>[a-z]{2,}[A-Z]{2,}]', ''))

    word_amounts = word_amounts.select(explode(split(word_amounts.words, "\s+")).alias('word')).groupBy('word').count()
    word_amounts = word_amounts.sort('count', ascending=False)
    word_amounts = word_amounts.filter(length(col('word')) > 5)

    features = word_amounts.toPandas()
    features_from_top = features.loc[:19]
    features_random = features.loc[20:].sample(0)
    features = pd.concat([features_from_top, features_random])

    features.to_csv('E:\\stud\\spark\\features\\' + title[:title.index('.')] + '_features.txt', encoding='utf-8')
    word_amounts.toPandas().to_csv('E:\\stud\\spark\\words\\' + title + '_words.txt', encoding='utf-8')
