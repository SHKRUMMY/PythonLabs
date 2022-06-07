import re
from zipfile import ZipFile

regex = re.compile('" 304')
with ZipFile('access_log.zip', 'r') as zipObj:
    zipObj.extractall()

with open("result.txt", "w") as result_file:
    with open('access_log', 'r') as file:
        for line in file:
            if regex.search(line) is not None:
                result_file.write(line)