# Author : virualv
# Time : 9/15/2018 1:34 PM

import time

# print(help(time))
#
# print(time.time())          # 1536989770.797348 时间戳  ******

# time.sleep(3)               #                           ******

# print(time.clock())           # 计算CPU执行时间
                              # warning: time.clock has been deprecated in Python 3.3 and will be removed from Python 3.8
# print(time.process_time())  # use time.perf_counter or time.process_time instead

# print(time.gmtime())        # time.struct_time(tm_year=2018, tm_mon=9, tm_mday=15, tm_hour=5, tm_min=50, tm_sec=36, tm_wday=5, tm_yday=258, tm_isdst=0)
                              # UTC

# print(time.localtime())       # 本地时间 UTC+8            ******

# print(time.strftime('%Y-%m-%d %I:%M:%S %p',time.localtime()))       # 2018-09-15 02:38:46 PM # *******
# print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))          # 2018-09-15 14:38:46

#print(help(time.strftime))
#     %Y  Year with century as a decimal number.
#     %m  Month as a decimal number [01,12].
#     %d  Day of the month as a decimal number [01,31].
#     %H  Hour (24-hour clock) as a decimal number [00,23].
#     %M  Minute as a decimal number [00,59].
#     %S  Second as a decimal number [00,61].
#     %z  Time zone offset from UTC.
#     %a  Locale's abbreviated weekday name.
#     %A  Locale's full weekday name.
#     %b  Locale's abbreviated month name.
#     %B  Locale's full month name.
#     %c  Locale's appropriate date and time representation.
#     %I  Hour (12-hour clock) as a decimal number [01,12].
#     %p  Locale's equivalent of either AM or PM.

# print(time.strptime('2018-09-15 14:38:46','%Y-%m-%d %H:%M:%S')) # ******
# a = time.strptime('2018-09-15 14:38:46','%Y-%m-%d %H:%M:%S')
# print(a.tm_year,a.tm_mon,a.tm_wday)

# print(time.ctime())               # *****
# print(time.ctime(10))             # 加时间戳

# print(help(time.mktime))
# print(time.mktime(time.localtime())) # 计算时间戳，精确到秒
