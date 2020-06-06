# downloading files from the web using python

import requests 


#requests.get()
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
# status code 200 corresponds to everything being ok - 404 corresponds to file not being found
if res.status_code == 200:
    print("success")
else:
    print("request unsuccessful")

print(len(res.text))
print()
print()
print(res.text[:500])
print()


#res.raise_for_status()      # raises an exception if there was an error downloading the file
#badRes = requests.get('https://automatetheboringstuff.com/files/abcdefg')
#badRes.raise_for_status()      # halts program status

# Python and Unicode:       http://bit.ly/unipain
playFile = open('RomeoAndJuliet.txt', 'wb')     # This allows us to download a file in chunks and then write it to a file in the cwd
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()