# While working with an API service, they allow a comma-delimited list of values
# with a maximum length of 10. While deciding whether or not to raise an error
# if the length > 10 and block the call, I decided to make multiple calls to the
# service.
#
# If n is omitted, this will create one group of all values.

def delimited_groups(data, n=10, copy=False):
	groups = []

	if copy:
		list_ = list(data)
	else:
		list_ = data
	n = len(list_) if n == 0 else n

	if len(list_) < n:
		groups.append(','.join(list_))
	else:
		while len(list_) > 0:
			groups.append(','.join(list_[:n]))
			del list_[:n]

	return groups