import http.client
import time

connection = http.client.HTTPConnection("python-test-server:8080")

while True:
    time.sleep(0.5)
    connection.request("GET", "/")
    response = connection.getresponse()
    print("status: {} and reason: {}".format(response.status, response.reason))

connection.close()
