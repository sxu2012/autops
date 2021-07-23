#hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar \
#-file /home/hdfs/mapper1.py    -mapper /home/hdfs/mapper1.py \
#-file /home/hdfs/reducer1.py   -reducer /home/hdfs/reducer1.py \
#-input /autops/input/data.csv \
#-output /autops/output/all_accidents

#-file option is deprecated, with or without produces the same error result
hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -mapper /home/hdfs/mapper1.py -reducer /home/hdfs/reducer1.py -input /user/jxu/data.csv -output /user/jxu/all_accidents