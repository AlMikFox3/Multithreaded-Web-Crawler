import os

def create_project_dir(directory):
	if not os.path.exists(directory):
		print ('Creating Directory : '+ directory)
		os.makedirs(directory)

def create_data_files(project_name, base_url):
	queue = os.path.join(project_name , 'queue.txt')
	crawled = os.path.join(project_name,"crawled.txt")
	if not os.path.isfile(queue):
		write_file(queue, base_url)
	if not os.path.isfile(crawled):
		write_file(crawled, '')

def write_file(path, data):
	f = open(path,'w')
	f.write(data)
	f.close

def append_to_file(path, data):
	with open(path,'a') as file:
		file.write(data + '\n')

def delete_from_file(path):
	with open(path,'w'):
		pass #Create a blank file (hence previous contents deleted)

def file_to_set(file_name):
	results = set()
	with open(file_name,'rt') as f:
		for line in f:
			results.add(line.replace('\n',''))
	return results

def set_to_file(links, file):
	with open(file,"w") as f:
		for l in sorted(links):
			f.write(l+"\n")








