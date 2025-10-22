from http.server import HTTPServer,BaseHTTPRequestHandler


content = """
<!DOCTYPE html>
<html>
    <head>
        <title>LAPTOP DETAIL</title>
    </head>
    <body align="center">
        <h1>Sri Saran</h1>
        <h1>MY REGISTER NO:25015592</h1>
    <table border="5" cellspacing="5" cellpadding="5" align="center" >
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
