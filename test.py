# show the log on the terminal when there is changes on the 
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

if __name__=="__main__":
    # logging.basicConfig
    # level = INFO
    # sets the threshold for this loger to level
    # Logging messages which are less severe than level will be ignored
    # logging messages which have severity level or higher will be emitted by
    # whichever handler or handlers service this logger


    # format = asctime - message
    # datefmt = year, month, day, hour, minute, and seconds
    logging.basicConfig(level=logging.INFO, # level = logging.INFO
                        format='%(asctime)s-%(message)s', # asctime - message
                        # year, month, day, hour, minute, and second
                        datefmt="%Y-%m-%d %H:%M:%S") 
                        
    path = "/home/joshep/Desktop/myFolder"
    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        while True:
            # 0.001 sec delay for every single check
            time.sleep(1)
    except KeyboardInterrupt:
        # when keyboardinterrupt occured, observer stops working
        observer.stop()
    observer.join()