from concurrent.futures import ThreadPoolExecutor
import time,requests

threadcount=5 # Number of threads
url='http://rakeshmane.com/xss.js'

def hit_url(count):

    print "\nSending request number : ",count
    resp=requests.get(url,allow_redirects=False,verify=False,proxies={"http":"http://127.0.0.1:8080"})
    return resp


with ThreadPoolExecutor(max_workers=threadcount) as executor:
    count=0
    while True:
        future=executor.submit(hit_url,count)
        count=count+1

# Press Ctrl+C to exit.
