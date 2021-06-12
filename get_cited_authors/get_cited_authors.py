def get_cited_authors(text_file):
	"""parses the Web of Science text_file for the Cited References section and returns a dictionary list of authors with counts for each author (sorted by number of occurrences, all uppercase)"""
	
	from collections import Counter
	
	cited_authors  = []
	with open (text_file, 'rt') as citefile:
		cr_flag = False
		for line in citefile:
			if cr_flag:
				if line[:2] == "  ":
					cited_authors.append(line.split(",")[0][3:].upper())
				else:
					cr_flag = False
			elif line[:2] == "CR":
				cr_flag = True
				cited_authors.append(line.split(",")[0][3:].upper())
	author_count = Counter(cited_authors)
	return author_count
