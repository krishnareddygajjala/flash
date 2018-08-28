
import logging
#import os


LOG_FILENAME  = 'log1.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.INFO)
logger = logging.getLogger(__name__)
logging.debug('This message should go to the log file')
logging.info('So should this')  # will not print anything
logging.warning('And this, too') # will print a message to the console

logging.info('creating a list upto 10 numbers')
lst = list(range(11))

logging.info('printing a complete list') # update records here
print lst  
logger.info("printing each element in a list using for loop")
for i in lst:
    print i
logger.info("printed successfully")

