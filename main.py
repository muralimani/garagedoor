import machine

try:
    import socket
    import time
    from machine import Timer
    from machine import Pin

    def do_connect():
        import network
        sta_if = network.WLAN(network.STA_IF)
        if not sta_if.isconnected():
            print('connecting to network...')
            sta_if.active(True)
            sta_if.connect('XXX', 'XXX')
            while not sta_if.isconnected():
                pass

    def web_page():
        html = """<html><head> <title>Garage Door Opener</title> <meta name="viewport" content="width=device-width, initial-scale=1"><link rel="icon" href="data:,"> <style>html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;} h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}.button{display: inline-block; background-color: #e7bd3b; border: none; border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;} button2{background-color: #4286f4;}</style></head><body> <h1>Garage Door</h1><p><a href="/?door=open"><button class="button">Click to Open/Close</button></a></p></body></html>"""
        return html

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 80))
    s.listen(5)

    while True:
        do_connect()
        conn, addr = s.accept()
        print('Got a connection from %s' % str(addr))
        request = conn.recv(1024)
        request = str(request)
        print('Content = %s' % request)
        door_open = request.find('/?door=open')
        if door_open > 0:
            print('DOOR OPEN')
            p1 = Pin(26,Pin.OUT)
            time.sleep(2)
            p1.value(0)
            time.sleep(2)
            p1.value(1)
            time.sleep(1)
        response = web_page()
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: text/html\n')
        conn.send('Connection: close\n\n')
        conn.sendall(response)
        conn.close()
except:
  machine.reset()