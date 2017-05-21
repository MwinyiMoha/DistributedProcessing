# DistributedProcessing
Showcasing multiprocessing and distributed processing in python. Well DistributedProcessing is a little bit fancy but no problem.

Multiprocessing In Python

Multiprocessing is a package in python that enables spawning of processes through an API. It aims at achieving parallelism in processing which can provide a huge performance boost in the right scenario. In this test, i generate random numbers, put them in a list and sum them up. For those of us conversant with algorithms and the Big O Notation, will agree with me that this procedure is dependent on the value of N. The bigger the value of N, the more the work.


Computer Specifications

This test was carried out on a HP Probook 4520s with the following specs:
	*Intel Core i5 Processor at 2.5GHz (4 cores)
	*4 GB RAM
	*Windows 7 Ultimate, Service Pack 1
	*Python 2.7


The Single Core Approach

Demonstrated by the script 'singlecore.py', it takes the value of N as a parameter to generate N random integers with value ranging 0-10. The integers are returned in a list then summed up. This all happens within a single process. Running times for the script written to file were as follows:

	Value of N(000)		Time Taken
	1			            0.0
	10			          0.0310001373291 
	100			          0.358000040054 
	1000			        3.40100002289 
	10000			        20.4990000725 

The script returned a memory error with the value of N at 100,000,000

The Multiprocessing Approach

Demonstrated by 'multicore.py', it takes the value of N as a parameter to generate N random integers with value ranging 0-10. The integers are returned in a list then summed up. However, this time i leverage a Pool spawnign 4 process to hopefully avail each process to a core. Each process and therefore each processor core gets a quarter of the load (N). The four intermediate results from each process are then merged to give the final result. Running times for the script written to file were as follows:

	Value of N(000)		Time Taken
	1			            0.374000072479 
	10			          0.375 
	100			          0.593000173569 
	1000			        1.91899991035 
	10000			        10.3120000362

The script returned a memory error with the value of N at 1,000,000,000


My Comparison

So, multiprocessing starts out slow, taking longer with lower values of N(0.59 seconds at 100,000 compared to 0.35 seconds scored by the single process at the same value of N). However, the tables turn at 1,000,000 when multiprocessing takes 1.9 seconds compared to 3.4 seconds scored by the single process. At 10,000,000 the 4 processes take half the time it takes the single process to finish.

Whats more interesting is that multiprocessing runs out of memory at N=1,000,000,000. Correct, it can process 100,000,000 integers which took a little over 86 seconds. Is this evidence of better memory management when using multiple processes?? The correct answer is, am yet to validate that. 

So what about CPU and RAM usage??

Well, Windows 7 has these nice little gadgets one of which happens to show CPU and RAM usage. So I rebooted my pc and monitored these resource values at idle, when running singlecore at N=10,000,000 and when running multicore at N=10,000,000. Here are the results:

	State		Peak CPU(%)	Peak RAM(%)
	Idle		    2		      33
	Singlecore	30		    41
	Multicore 	98		    46(from 41)

Interesting, right?? So it happens that after running singlecore.py with N=10,000,000 the RAM value did not revert to 33% but stuck at 41%. In my conclusion the values hint at multiprocesses being slow for small loads and quite fast for larger loads. Again, multiprocesses utilize maximum resources for a short time while a single process would utilize partial resources for a longer time. I guess these are the trade-offs that would make parallelism suitable or unsuitable for a particular scenario.


Plotter.py??

This is a simple script tool that reads the text files written by the other script tools and plots two graphs of N against Time. Where i come from, visual representation of such interesting concept is highly encouraged. So if you happen to take this test on, feel free to use the plotter and see the interesting graph that appears.

*Note that you should have matplotlib installed for this script to run.

The Geospatial Realm

Well, I happen to be a Geospatial Developer and whenever i stumble upon such interesting concepts I try to relate them to the Geospatial world. So lets say I have this Vector File Converter Script which can comfortably convert a shapefile to geojson, what if i give it 5, 10, 20, 40, 80 shapefiles to convert in a single process setup and then in a multiple process setup. What are the odds that multiple processes will take less time to convert the 80 shapefiles than the single process?? Only one way to find out... 

#References and Further Reading


