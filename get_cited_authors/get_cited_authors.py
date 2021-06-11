def get_cited_authors(text_file):
	"""parses the Web of Science text_file for the Cited References section and returns a list of authors (unsorted, in various capitalizations, containing duplicates)"""
	
	cited_authors  = []
	with open (text_file, 'rt') as citefile:
		cr_flag = False
		for line in citefile:
			if cr_flag:
				if line[:2] == "  ":
					cited_authors.append(line.split(",")[0][3:])
				else:
					cr_flag = False
			elif line[:2] == "CR":
				cr_flag = True
				cited_authors.append(line.split(",")[0][3:])
	return cited_authors

yulia_cr = get_cited_authors("sample.txt")
print(yulia_cr)