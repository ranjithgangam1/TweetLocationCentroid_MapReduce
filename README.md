# TweetLocationCentroid_MapReduce
# TweetLocationCentroid_MapReduce

###This map reduce program runs on twitter data collected for last one year. This program do the following thing
###For those tweets with location information, what lat/long (or city/state) is the centroid? What was the proportion of tweets with location to those without?

###Approach:

I chose streaming-mode. I have done Map and Reduce jobs in python. I wrote map_loc.py and red_loc.py files.

###Mapper explanation:

Mapper reads each tweet from HDFS file system and checks for “id” which is a key and also for “coordinates” which is a value from the mapper output. It gives a value None if there is no coordinates for the tweet otherwise it gives coordinates of the tweet with lat/long values.

###Mapper output:

First Mapper output: &lt;id&gt;\t&lt;cordinates&gt;

Example mapper output:

489238428131663872 [-84.293721000000005, 39.566229999999997]

489238442539098113 None

###Reducer explanation:

Reducer will get the input of id and coordinator value and it separates None values with their count and lat/long values with their count. To find the centroid, it finds the sum of all lat and long values separately and send them through the formula. It gives an output of the centroid and proportion answer for the given question. Counts are used for the proportion.

Reducer output &lt;centroid&gt; &lt;proportion&gt;

Output:

Created a run7.sh file to run the application using the mentioned commands in the lecture in

it.

Reducer output from HDFS is stored in the “outputLOC” folders.

Output:

Centroid (-82.452943520467116, 38.99033843275194)

Proportion% 44.3566476733
