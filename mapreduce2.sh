#hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar \
#-file /home/hdfs/mapper2.py    -mapper /home/hdfs/mapper2.py \
#-file /home/hdfs/reducer2.py   -reducer /home/hdfs/reducer2.py \
#-input output/all_accidents \
#-output output/make_year_count
hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar \
   -mapper /home/hdfs/mapper2.py \
   -reducer /home/hdfs/reducer2.py \
   -input output/all_accidents \
   -output output/make_year_count