delimited_groups
================

This was made in answer to an API service only allowing a maximum of 10 items to
be passed in a comma-delimited string.

```python
class caller(_service):

	def add_tags(self, tags):
		parameters = []
		tag_groups = delimited_groups(tags, 10)
		for i in tag_groups:
			parameters.append({'tags': tag_group[i]})
		return self.multi_request('post', 'image.add_tags', parameters)
```

This will generate groups of 10 comma-delimited tags to be sent to the service.
the .multi_request() creates requests for all parameters[n]