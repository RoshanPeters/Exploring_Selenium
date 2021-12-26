'''
Every action or event will be stored/logged into the log file.
By looking at the log file we can see all the actions so that it can be used for debugging.
Logging can help you develop a better understanding of the flow of a program and discover scenarios that you might not even have thought of while developing.

Log levels:
 debug
 info 
 warning
 error
 critical
we can generate logs in different levels
'''
import logging 

logging.basicConfig(filename="test.log", level=logging.DEBUG, format='%(asctime)s: %(levelname)s: %(message)s')  # logging.DEBUG will help display all the levels

logging.debug('this is debug message')
logging.info('this is info message')
logging.warning('this is warning message')  # the default threshold is from warning message
logging.error('this is error message')
logging.critical('this is critical message')

'''
Another way to change the threshold/set the level:

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
'''