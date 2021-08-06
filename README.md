watchdog
1. recursive detection for changes in the folder
	- Create an instance of the watchdog.observers.Observer thread class
	- Implement a subclass of watchdog.events.FileSystemEventHandler
	- Schedule monitoring a few paths with the observer instance attaching the event handler.
	- Start the observer thread and wait for it generate event without blocking our main thread.

By default, an watchdog,observers.Observer instance will not monitor sub-directories. By passing recursive=True in the call to watchdog.observers.Observer.schedule() monitoring entire directory trees is ensured. --> when recursive = True is passed in the schedule, then the monitoricng entire directory trees will be ensured
