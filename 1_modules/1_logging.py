# Author : virualv
# Time : 9/17/2018 10:45 PM
import logging

# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                     datefmt='%a, %d %b %Y %H:%M:%S',
#                     filename='test.log',
#                     filemode='a')

# Tue, 18 Sep 2018 10:51:38 1_logging.py[line:14] DEBUG debug message

# logging.debug('debug message')
# logging.info('info message')
# logging.warning('warning message')
# logging.error('error message')
# logging.critical('critical message')

import logging

logger = logging.getLogger()
# 创建一个handler（处理器），用于写入日志文件
fh = logging.FileHandler('test.log')

# 再创建一个handler（处理器），用于输出到控制台
ch = logging.StreamHandler()

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.addHandler(fh)   # logger对象可以添加多个fh和ch对象
logger.addHandler(ch)

logger.setLevel(logging.DEBUG)
logger.debug('logger debug message')
# logger.info('logger info message')
# logger.warning('logger warning message')
# logger.error('logger error message')
# logger.critical('logger critical message')







# logger = logging.getLogger()
#
# fp = logging.FileHandler()
# sp = logging.StreamHandler()
#
# formatter = logging.Formatter('%(asctime)s - %(lineno)d - %(levelname)s - %(message)s')
#
# fp.setFormatter(formatter)
# sp.setFormatter(formatter)
#
# logger.addHandler(fp)
# logger.addHandler(sp)


















