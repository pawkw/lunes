# Lunes tutorial

## Using Python's interactive mode

Start the program in Python's interactive mode using `python -i lunes.py`. You can exit the interactive shell using `exit()`. It will pause for a moment as it calculates every lune in the year, then it will print out a summary of the year and then go to the Python prompt. An object named `year` will be available.

```
1 Start: 2018/3/17 07:51:00 end: 2018/4/16 07:19:41 lunes: 29
2 Start: 2018/4/16 07:19:41 end: 2018/5/15 06:25:27 lunes: 28
3 Start: 2018/5/15 06:25:27 end: 2018/6/13 05:43:11 lunes: 28
4 Start: 2018/6/13 05:43:11 end: 2018/7/13 06:25:08 lunes: 29
5 Start: 2018/7/13 06:25:08 end: 2018/8/11 06:25:44 lunes: 28
6 Start: 2018/8/11 06:25:44 end: 2018/9/9 06:30:30 lunes: 28
7 Start: 2018/9/9 06:30:30 end: 2018/10/9 07:45:57 lunes: 29
8 Start: 2018/10/9 07:45:57 end: 2018/11/7 06:45:21 lunes: 28
9 Start: 2018/11/7 06:45:21 end: 2018/12/7 07:44:46 lunes: 29
10 Start: 2018/12/7 07:44:46 end: 2019/1/6 08:16:49 lunes: 29
11 Start: 2019/1/6 08:16:49 end: 2019/2/4 07:36:22 lunes: 28
12 Start: 2019/2/4 07:36:22 end: 2019/3/6 07:10:19 lunes: 29
==========
Start: 2018/3/17 07:51:00 end: 2019/3/6 07:10:19 months: 12 lunes: 342
```

## Using detail(), summary() or print on a month

Next, let's take a look at the first month in detail:

```
>>> year.month(1).detail()
1/1: Start: 2018/3/17 07:51:00 end: 2018/3/18 08:19:49 hours: 24.48 phase: 0.00
1/2: Start: 2018/3/18 08:19:49 end: 2018/3/19 08:49:11 hours: 24.49 phase: 0.01
1/3: Start: 2018/3/19 08:49:11 end: 2018/3/20 09:20:21 hours: 24.52 phase: 0.05
1/4: Start: 2018/3/20 09:20:21 end: 2018/3/21 09:54:38 hours: 24.57 phase: 0.10
1/5: Start: 2018/3/21 09:54:38 end: 2018/3/22 10:33:33 hours: 24.65 phase: 0.18
1/6: Start: 2018/3/22 10:33:33 end: 2018/3/23 11:18:34 hours: 24.75 phase: 0.28
1/7: Start: 2018/3/23 11:18:34 end: 2018/3/24 12:10:44 hours: 24.87 phase: 0.39
1/8: Start: 2018/3/24 12:10:44 end: 2018/3/25 13:10:08 hours: 24.99 phase: 0.50
1/9: Start: 2018/3/25 13:10:08 end: 2018/3/26 14:15:36 hours: 25.09 phase: 0.62
1/10: Start: 2018/3/26 14:15:36 end: 2018/3/27 15:24:59 hours: 25.16 phase: 0.74
1/11: Start: 2018/3/27 15:24:59 end: 2018/3/28 16:35:59 hours: 25.18 phase: 0.83
1/12: Start: 2018/3/28 16:35:59 end: 2018/3/29 17:46:51 hours: 25.18 phase: 0.91
1/13: Start: 2018/3/29 17:46:51 end: 2018/3/30 18:56:37 hours: 25.16 phase: 0.97
1/14: Start: 2018/3/30 18:56:37 end: 2018/3/31 20:04:52 hours: 25.14 phase: 0.99
1/15: Start: 2018/3/31 20:04:52 end: 2018/4/1 21:11:28 hours: 25.11 phase: 1.00
1/16: Start: 2018/4/1 21:11:28 end: 2018/4/2 22:16:15 hours: 25.08 phase: 0.97
1/17: Start: 2018/4/2 22:16:15 end: 2018/4/3 23:18:54 hours: 25.04 phase: 0.92
1/18: Start: 2018/4/3 23:18:54 end: 2018/4/5 00:18:48 hours: 25.00 phase: 0.86
1/19: Start: 2018/4/5 00:18:48 end: 2018/4/6 01:15:13 hours: 24.94 phase: 0.78
1/20: Start: 2018/4/6 01:15:13 end: 2018/4/7 02:07:22 hours: 24.87 phase: 0.69
1/21: Start: 2018/4/7 02:07:22 end: 2018/4/8 02:54:47 hours: 24.79 phase: 0.60
1/22: Start: 2018/4/8 02:54:47 end: 2018/4/9 03:37:22 hours: 24.71 phase: 0.50
1/23: Start: 2018/4/9 03:37:22 end: 2018/4/10 04:15:29 hours: 24.64 phase: 0.41
1/24: Start: 2018/4/10 04:15:29 end: 2018/4/11 04:49:51 hours: 24.57 phase: 0.31
1/25: Start: 2018/4/11 04:49:51 end: 2018/4/12 05:21:21 hours: 24.53 phase: 0.22
1/26: Start: 2018/4/12 05:21:21 end: 2018/4/13 05:51:00 hours: 24.49 phase: 0.15
1/27: Start: 2018/4/13 05:51:00 end: 2018/4/14 06:19:52 hours: 24.48 phase: 0.08
1/28: Start: 2018/4/14 06:19:52 end: 2018/4/15 06:49:01 hours: 24.49 phase: 0.03
1/29: Start: 2018/4/15 06:49:01 end: 2018/4/16 07:19:41 hours: 24.51 phase: 0.01
==========
Start: 2018/3/17 07:51:00 end: 2018/4/16 07:19:41 lunes: 29
```

Printing the month prints the summary you see at the end of the details. This can also be done with the summary() method.

```
>>> print(year.month(1))
Start: 2018/3/17 07:51:00 end: 2018/4/16 07:19:41 lunes: 29
>>> year.month(1).summary()
Start: 2018/3/17 07:51:00 end: 2018/4/16 07:19:41 lunes: 29
```

## Using detail() or printing lunes.

You can see that 1/18 is a lune that wraps around a day. We can print out the detail of a single lune using the detail() method, or using print. There is no summary method for lunes:

```
>>> year.lune(1,18).detail()
Start: 2018/4/3 23:18:54 end: 2018/4/5 00:18:48 hours: 25.00 phase: 0.86
>>> print(year.lune(1,18))
Start: 2018/4/3 23:18:54 end: 2018/4/5 00:18:48 hours: 25.00 phase: 0.86
```

The 'phase' number is not the phase that we are used to. It is the percent of the surface of the moon that is illuminated at moonrise.

## Using detail(), summary() or printing the year.

The detail() method for the year object is what you get when the program starts. It prints out a summary for each month. The summary() method prints out the summary for the year. Using print on the year object does the same.

```
>>> year.summary()
Start: 2018/3/17 07:51:00 end: 2019/3/6 07:10:19 months: 12 lunes: 342
>>> print(year)
Start: 2018/3/17 07:51:00 end: 2019/3/6 07:10:19 months: 12 lunes: 342
```

## Using the find(month, day) method.

You can look up a date using the find(month, day) method.  It returns a tuple of the lune found.

```
>>> year.find(6,1)
(3, 17)
>>> print(year.lune(3,17))
3/17 Start: 2018/5/31 22:44:27 end: 2018/6/1 23:31:21 hours: 24.78 phase: 0.94
```

We can unpack this tuple and pass it directly to the lune(month, lune) method.

```
>>> year.lune(*year.find(6,1)).detail()
3/17 Start: 2018/5/31 22:44:27 end: 2018/6/1 23:31:21 hours: 24.78 phase: 0.94
```

There can be some weird problems because of fluid nature of the year start. Let's say that you were born March 1st at 7:10pm. Let's look up your birthday. The program starts by calculating the current year, which is 2018 as of this writing. I'll show the entire output from program start.

```
1 Start: 2018/3/17 07:51:00 end: 2018/4/16 07:19:41 lunes: 29
2 Start: 2018/4/16 07:19:41 end: 2018/5/15 06:25:27 lunes: 28
3 Start: 2018/5/15 06:25:27 end: 2018/6/13 05:43:11 lunes: 28
4 Start: 2018/6/13 05:43:11 end: 2018/7/13 06:25:08 lunes: 29
5 Start: 2018/7/13 06:25:08 end: 2018/8/11 06:25:44 lunes: 28
6 Start: 2018/8/11 06:25:44 end: 2018/9/9 06:30:30 lunes: 28
7 Start: 2018/9/9 06:30:30 end: 2018/10/9 07:45:57 lunes: 29
8 Start: 2018/10/9 07:45:57 end: 2018/11/7 06:45:21 lunes: 28
9 Start: 2018/11/7 06:45:21 end: 2018/12/7 07:44:46 lunes: 29
10 Start: 2018/12/7 07:44:46 end: 2019/1/6 08:16:49 lunes: 29
11 Start: 2019/1/6 08:16:49 end: 2019/2/4 07:36:22 lunes: 28
12 Start: 2019/2/4 07:36:22 end: 2019/3/6 07:10:19 lunes: 29
==========
Start: 2018/3/17 07:51:00 end: 2019/3/6 07:10:19 months: 12 lunes: 342
>>> year.lune(*year.find(3,1)).detail()
12/24 Start: 2019/2/28 03:20:03 end: 2019/3/1 04:11:37 hours: 24.86 phase: 0.32
```

The day found is in 2019! If you look at the year summary, you can see the year started on March 17th, so March 1st is in the previous year. Let's set the year to 2017 and try again.

```
>>> year = luneYear(2017)
>>> year.lune(*year.find(3,1)).detail()
1/3 Start: 2017/2/28 08:12:19 end: 2017/3/1 08:45:31 hours: 24.55 phase: 0.05
```

Now it's in 2017! The problem is that 2017 is a 13 month year that has March 1st twice. You can see this by using `year.summary()` or `year.detail()`. The find method returns the first instance it finds. We can tell it to specifically look in 2018.

```
>>> print(year.lune(*year.find(3,1,year = 2018)))
13/14 Start: 2018/2/28 16:42:53 end: 2018/3/1 17:55:55 hours: 25.22 phase: 0.98
```

Great! We found it. There is, however, another problem. If you look at the end time, you can see that it's March 1st at 5:55pm. We want 7:10pm. The find method allows you to specify hour, hour and minute, or hour and minute and second. If you include all the options, the year goes last year goes last without 'year='. Let's try it with just the hour and minute.

```
>>> print(year.lune(*year.find(3,1,19,10,year = 2018)))
13/15 Start: 2018/3/1 17:55:55 end: 2018/3/2 19:07:40 hours: 25.20 phase: 1.00
```

At last! We have found our date. You can also see that it's a full moon on that date.

## More fun.

While writing the find tutorial, I thought the process was a little ridiculous, so I added the printLunes() method. You gotta love Python. Ideas can be realized as you have them.

Let's say that you were born in 2000 and want to look up which lune that falls on for each year up to 2020.

```
>>> for x in range(2000, 2020):
...     luneYear(x).printLunes(3,1,19,10)
...
1/7 Start: 2001/3/1 10:13:18 end: 2001/3/2 10:48:14 hours: 24.58 phase: 0.35
13/17 Start: 2002/2/28 19:58:26 end: 2002/3/1 21:16:48 hours: 25.31 phase: 0.96
12/28 Start: 2003/3/1 06:45:06 end: 2003/3/2 07:12:18 hours: 24.45 phase: 0.03
1/11 Start: 2004/3/1 12:28:26 end: 2004/3/2 13:26:32 hours: 24.97 phase: 0.74
13/21 Start: 2005/2/28 23:10:31 end: 2005/3/2 00:24:28 hours: 25.23 phase: 0.77
1/2 Start: 2006/3/1 07:51:08 end: 2006/3/2 08:13:02 hours: 24.36 phase: 0.03
13/13 Start: 2007/3/1 15:55:21 end: 2007/3/2 17:02:23 hours: 25.12 phase: 0.96
12/23 Start: 2008/3/1 03:21:50 end: 2008/3/2 04:10:13 hours: 24.81 phase: 0.38
1/5 Start: 2009/3/1 08:37:05 end: 2009/3/2 09:10:12 hours: 24.55 phase: 0.21
13/15 Start: 2010/2/28 18:34:36 end: 2010/3/1 19:53:31 hours: 25.32 phase: 1.00
12/26 Start: 2011/3/1 05:10:09 end: 2011/3/2 05:37:51 hours: 24.46 phase: 0.11
1/10 Start: 2012/3/1 11:21:13 end: 2012/3/2 12:14:49 hours: 24.89 phase: 0.56
13/19 Start: 2013/2/28 21:42:01 end: 2013/3/1 22:51:44 hours: 25.16 phase: 0.88
1/1 Start: 2014/3/1 06:49:13 end: 2014/3/2 07:23:20 hours: 24.57 phase: 0.00
13/11 Start: 2015/3/1 14:39:10 end: 2015/3/2 15:35:35 hours: 24.94 phase: 0.87
12/22 Start: 2016/3/1 00:54:08 end: 2016/3/2 01:49:31 hours: 24.92 phase: 0.57
1/4 Start: 2017/3/1 08:45:31 end: 2017/3/2 09:20:13 hours: 24.58 phase: 0.11
13/15 Start: 2018/3/1 17:55:55 end: 2018/3/2 19:07:40 hours: 25.20 phase: 1.00
12/25 Start: 2019/3/1 04:11:37 end: 2019/3/2 04:57:16 hours: 24.76 phase: 0.23
```

If you're new to Python, the ellipses(...) appear on their own when you start a mutli-line statement. Remember to indent the second line and press enter on a blank line to start the process.

So we can see a whole bunch of month 13's because of the date. Let's look at the reverse. Your fictional birthday fell of 1/7 in 2000. This is your "birthlune". Let's go through each year and find out what day your birthlune falls on.

```
>>> for x in range(2000,2020):
...     print(luneYear(x).lune(1,7))
...
1/7 Start: 2000/3/12 11:37:25 end: 2000/3/13 12:26:11 hours: 24.81 phase: 0.43
1/7 Start: 2001/3/1 10:13:18 end: 2001/3/2 10:48:14 hours: 24.58 phase: 0.35
1/7 Start: 2002/3/20 10:45:43 end: 2002/3/21 11:27:08 hours: 24.69 phase: 0.35
1/7 Start: 2003/3/9 10:45:18 end: 2003/3/10 11:17:12 hours: 24.53 phase: 0.34
1/7 Start: 2004/2/26 09:57:05 end: 2004/2/27 10:24:38 hours: 24.46 phase: 0.36
1/7 Start: 2005/3/16 10:36:06 end: 2005/3/17 11:18:17 hours: 24.70 phase: 0.39
1/7 Start: 2006/3/6 10:13:16 end: 2006/3/7 11:00:43 hours: 24.79 phase: 0.48
1/7 Start: 2007/3/25 11:21:37 end: 2007/3/26 12:27:51 hours: 25.10 phase: 0.49
1/7 Start: 2008/3/13 10:39:14 end: 2008/3/14 11:37:34 hours: 24.97 phase: 0.41
1/7 Start: 2009/3/3 09:52:11 end: 2009/3/4 10:45:30 hours: 24.89 phase: 0.42
1/7 Start: 2010/3/21 10:02:20 end: 2010/3/22 10:56:25 hours: 24.90 phase: 0.30
1/7 Start: 2011/3/10 08:59:17 end: 2011/3/11 09:40:07 hours: 24.68 phase: 0.27
1/7 Start: 2012/2/27 09:18:30 end: 2012/2/28 09:53:38 hours: 24.59 phase: 0.28
1/7 Start: 2013/3/17 10:31:25 end: 2013/3/18 11:16:03 hours: 24.74 phase: 0.31
1/7 Start: 2014/3/7 10:29:04 end: 2014/3/8 11:14:58 hours: 24.77 phase: 0.41
1/7 Start: 2015/3/26 11:44:56 end: 2015/3/27 12:38:06 hours: 24.89 phase: 0.43
1/7 Start: 2016/3/15 12:14:33 end: 2016/3/16 13:08:43 hours: 24.90 phase: 0.50
1/7 Start: 2017/3/4 10:39:24 end: 2017/3/5 11:26:18 hours: 24.78 phase: 0.41
1/7 Start: 2018/3/23 11:18:34 end: 2018/3/24 12:10:44 hours: 24.87 phase: 0.39
1/7 Start: 2019/3/12 10:52:06 end: 2019/3/13 11:29:54 hours: 24.63 phase: 0.31
```

I hope that gives you some ideas. Have fun!

