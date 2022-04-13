hdfs dfs -rm -r /data
hdfs dfs -mkdir /data
hdfs dfs -put ~/movies.csv  /data
hdfs dfs -rm -r /data/output


yarn jar /usr/lib/hadoop/hadoop-streaming.jar -input /data/movies.csv -output /data/output -file ~/mapper.py ~/reducer.py -mapper "python3 mapper.py" -reducer "python3 reducer.py"

