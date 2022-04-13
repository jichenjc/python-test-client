import http.client
import time

connection = http.client.HTTPConnection("python-test-server")

while True:
    time.sleep(0.5)
    connection.request("GET", "/")
    response = connection.getresponse()
    print("Status: {} and reason: {}".format(response.status, response.reason))

connection.close()
