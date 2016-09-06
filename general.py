import os   #kind of used for creating directory

#Each website you crawl is a separate project(folder)


def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating project: '+directory)
        os.makedirs(directory)


# create_project_dir('thenewboston')


#url = r'https://thenewboston.com/'

#Create queue and crawled files(if not created)


def create_data_files(project_name,base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue,base_url)
    if not os.path.isfile(crawled):
        write_file(crawled,'')

#Create a new file


def write_file(path,data):
    f = open(path,'w')
    f.write(data)
    f.close()

#Clear file


def clean_file_contents(path):
    with open(path,'w'):
        pass#do nothing

#append data
def append_to_file(path,data):
    with open(path,'a') as file:
        file.write(data+'\n')


#Read a file and convert it to set
def file_to_set(file_name):
    results = set()
    with open(file_name,'rt') as file:
        for line in file:
            results.add(line.replace('\n',''))
    return results


#Iterate over set and write in file
def set_to_file(links,file_name):
    clean_file_contents(file_name)
    for link in links:
        append_to_file(file_name,link)


