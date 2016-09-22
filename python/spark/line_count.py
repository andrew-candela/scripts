#read the lines from the spark readme
from pyspark import SparkConf, SparkContext
conf=SparkConf().setMaster("local").setAppName("Andrews Spark")
sc=SparkContext(conf=conf)

def hasspark(line):
	return "Spark" in line

def haspython(x):
	return "Python" in x


lines=sc.textFile('/Users/acandela/spark/spark-1.6.2-bin-hadoop2.6/README.md')
l=lines.count()
splines=lines.filter(hasspark)
splines_count=lines.filter(hasspark).count()
pylines=lines.filter(haspython)

#combine rdds
union_rdd=pylines.union(splines)
#these are the lines that contain either spark or python.
#if a line contains spark and python, that line will be counted twice..
py_or_sp_lines=union_rdd.count()

#count lines locally
vals=union_rdd.countByValue()

unique_vals=len(vals.keys())

print("there are {} lines total, and {} of them contain 'Spark'".format(l,splines_count))
print("there are {} lines that contain 'Python', and there are {} lines that conatin 'Spark' or 'Python', {} of them are unique".format(pylines.count(),py_or_sp_lines,unique_vals))

