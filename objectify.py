import json
 
class objectify:

	def __init__(self, data, node=None):
		if isinstance(data, str):
			data = json.loads(data)
		if node:
			self.data = data[node]
		else:
			self.data = data
		
	def __getattr__(self, key):
		if key in self.data:
			if isinstance(self.data[key], (list, dict)):
				return objectify(self.data[key])
			else:
				return self.data[key]
		else:
			raise Exception('There is no data[\'{key}\'].'.format(key=key))
			
	def __getitem__(self, key):
		if key in self.data:
			return self.data[key]
		else:
			raise Exception('There is no data[\'{key}\'].'.format(key=key))
	
	def __len__(self):
		return len(self.data)

	def __repr__(self):
		return '%r' % (self.__dict__['data'])
		
	def __str__(self):
		return '%r' % (self.__dict__['data'])
