#! /usr/bin/env /usr/bin/python

import multiprocessing
import time

class DupKlass(object):
    """
    start of dupklass -> class
    """
    COUNT = 2
    def __init__(self, myid):
        self._id = myid
	#print "Object created with myid :", self._id
   

    def __str__(self):
        return "Object : {0}".format(self._id)


    @classmethod
    def count(klass):
        return klass.COUNT


    def __call__(self):
        """
	 Make object as callable
	"""
        print self, "invoked"


    def start(self):
        print "Just started @", time.time() 
	time.sleep(1)
	print "Just ended @", time.time()


def main():
    count = DupKlass.count()
    kls = [DupKlass(i+1) for i in range(count)]

    # Below lines print's the object content instead of name
    #print kls[0]
    #print kls[1]

    #invoking the object as method
    #kls[0]()
    #kls[1]()

    threads = []
    threadnames = ["TARGET1", "TARGET2"]
    i = 0

    for obj in kls:
        thread = multiprocessing.Process(target=obj.start, name=threadnames[i])
        threads.append(thread)
	i += 1

    for thread in threads:
        thread.start()
        thread.join(2.0)
	print "STATUS of {0} : {1}".format(thread.name, thread.is_alive())
	if thread.is_alive():
	    print "Sent TERMINATION to :", thread.name
	    thread.terminate()
        #thread.join()
	print "STATUS of {0} : {1}".format(thread.name, thread.is_alive())

#    for thread in threads:
#        thread.join(1.0)
#        i += 1

if __name__ == '__main__':
    main()
