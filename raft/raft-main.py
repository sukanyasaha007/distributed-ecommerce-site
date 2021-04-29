from pysyncobj import SyncObj
from pysyncobj.batteries import ReplCounter, ReplDict


class MyCounter(SyncObj):
	def __init__(self):
		super(MyCounter, self).__init__('10.0.0.35:5000', ['10.0.0.36:6000', '10.0.0.37:7000'])
		self.__counter = 0
		self.selfNode= '10.0.0.26:5000'

	@replicated
	def incCounter(self):
		self.__counter += 1

	def getCounter(self):
		return self.__counter

counter1 = ReplCounter()
counter2 = ReplCounter()
dict1 = ReplDict()
syncObj = SyncObj('0.0.0.0:5000', ['0.0.0.0:6000', '0.0.0.0:7000'], consumers=[counter1, counter2, dict1])

counter1.set(42, sync=True) # set initial value to 42, 'sync' means that operation is blocking
counter1.add(10, sync=True) # add 10 to counter value
counter2.inc(sync=True) # increment counter value by one
dict1.set('testKey1', 'testValue1', sync=True)
dict1['testKey2'] = 'testValue2' # this is basically the same as previous, but asynchronous (non-blocking)
print(counter1, counter2, dict1['testKey1'], dict1.get('testKey2'))