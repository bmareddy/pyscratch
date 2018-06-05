from timeit import Timer
import Fibo

t1 = Timer("fibr(10)","from Fibo import fibr")

for i in range(1,41):
	s = "fibr(" + str(i) + ")"
	t1 = Timer(s,"from Fibo import fibr")
	time1 = t1.timeit(1)
	s = "fibi(" + str(i) + ")"
	t2 = Timer(s,"from Fibo import fibi")
	time2 = t2.timeit(1)
	print("n=%2d, fib: %8.6f, fibi:  %7.6f, percent: %10.2f" % (i, time1, time2, time1/time2))