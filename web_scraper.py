import requests, bs4, os
from pathlib import Path

print("Getting source webpage")
#Get source web page
res = requests.get('http://pages.cs.wisc.edu/~shivaram/cs744-fa18/')

#Convert to beautiful soup object
bs4_obj = bs4.BeautifulSoup(res.text, features="html.parser")

#use beautiful soup to extract all anchor tags
elems = bs4_obj.select('a')

#save the anchor tags that contain a pdf file extension into a list called links
links = []
for elem in elems:
    if ".pdf" in str(elem):
        links.append(elem['href'])

#create a folder to store the files
path = 'pdfs'

try:
    os.makedirs(path)
except OSError:
    print ("Creation of the directory %s failed" % path)
else:
    print ("Successfully created the directory %s " % path)

    #Download and save the file to the disk
    for link in links:
        print('Downloading pdf %s...' %(link))
        response = requests.get(link)
        file_to_save = open(os.path.join(path, os.path.basename(link)), 'wb')
        
        for chunk in response.iter_content(100000):
            file_to_save.write(chunk)

        file_to_save.close()

    num_files = len(links)
    print(f"All pdf's saved. Total number {len(links)}")


