from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split, regexp_replace, concat, lower, col

spark = SparkSession.builder.getOrCreate()

textFile = spark.read.text("E:\\stud\\spark\\md.txt")
textFile = textFile.withColumn('value', regexp_replace('value', r'^[-+]?[0-9]+$', ''))
textFile = textFile.filter(textFile.value != '')

wordCounts = textFile.select(lower(col('value')).alias('words'))
wordCounts = wordCounts.withColumn('words', regexp_replace('words', r'[!–.,?:;"»<>]', ''))
wordCounts = wordCounts.select(explode(split(wordCounts.words, "\s+")).alias('word')).groupBy('word').count()
wordCounts.toPandas().to_csv('words.csv')
