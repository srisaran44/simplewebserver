# EX01 Developing a Simple Webserver
## Date:06-10-2025

## AIM:
To develop a simple webserver to serve html pages and display the Device Specifications of your Laptop.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
```
from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
    <head>
        <title>LAPTOP DETAIL</title>
    </head>
    <body align="center">
        <h1>Srisaran</h1>
        <h1>MY REGISTER NO:25015592</h1>
        <table border="5" cellspaceing="5" cellpading="5" align="center" >
        <tr bgcolor="green">
            <th>S NO</th>
            <th>DEVICE SPECIFICATION</th>
            <th>DEVICE DETAIL</th>
        </tr>
        <tr>
            <td>1</td>
            <td>STORAGE</td>
            <td>1024 GB</td>
        </tr>   
        <tr>
            <td>2</td>
            <td>RAM</td>
            <td>16 GB</td>
        </tr>
        <td>3</td>
        <td>PROCESSOR</td>
        <td>INTEL CORE ULTRA 5</td>
        <tr>
            <td>4</td>
            <td>EDITION</td>
            <td>Windows 11 Home Single Language</td>
        </tr>
        <tr>
            <td>5</td>
            <td>SYSTEM TYPE</td>
            <td>64-bit operating system, x64-based processor</td>
        </tr>
        </table>
    </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()

```
## OUTPUT:

![alt text](<project1/app1/Screenshot 2025-10-06 220818.png>)
![alt text](<Screenshot 2025-10-22 224729.png>)
## RESULT:
The program for implementing simple webserver is executed successfully.
