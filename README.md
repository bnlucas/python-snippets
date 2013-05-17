Func: delimited_groups(list data [, int n, bool copy])
------------------------------------------------------

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

Class: objectify(mixed data [, string node])
--------------------------------------------

When I am working with JSON objects and I know the structure of them, I find the
current `dict` way a little more time consuming than say if it were an object.

```python
results = '''
{
   "exam_one":{
      "student_a":{
         "a":1,
         "b":3,
         "c":2,
         "d":2,
         "e":4
      },
      "student_b":{
         "a":2,
         "b":3,
         "c":2,
         "d":3,
         "e":1
      }
   }
}
'''

exams		= objectify(results) # full JSON object.
# print exams.exam_one.student_a.a
# print exams['exam_one']['student_a']['a']

exam_one	= objectify(results, 'exam_one') # only get exam_one node.
# print exam_one.student_a.a
# print exam_one['student_a']['a']
```

Both new and old methods `object.node.node` and `object['node']['node']` work so
this can be added into any script that uses `json`

This also works with regular `dict` objects as well.