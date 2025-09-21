import network
import socket
import time
from machine import Pin, time_pulse_us

# Wi-Fi credentials
SSID = 'vivo V50'
PASSWORD = '12340000'

# Login credentials
USERNAME = 'admin'
PASSWORD_AUTH = '1234'

session_authenticated = False

# Motor pins
AIN1 = Pin(25, Pin.OUT)
AIN2 = Pin(33, Pin.OUT)
BIN1 = Pin(27, Pin.OUT)
BIN2 = Pin(14, Pin.OUT)
PWMA = Pin(32, Pin.OUT)
PWMB = Pin(12, Pin.OUT)
STBY = Pin(26, Pin.OUT)

PWMA.on()
PWMB.on()
STBY.on()

# Ultrasonic sensor pins
TRIG = Pin(2, Pin.OUT)
ECHO = Pin(4, Pin.IN)

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    while not wlan.isconnected():
        time.sleep(1)
    print("Connected, IP:", wlan.ifconfig()[0])
    return wlan.ifconfig()[0]

def move_forward():
    AIN1.on(); AIN2.off()
    BIN1.on(); BIN2.off()

def move_backward():
    AIN1.off(); AIN2.on()
    BIN1.off(); BIN2.on()

def move_left():
    AIN1.off(); AIN2.on()
    BIN1.on(); BIN2.off()

def move_right():
    AIN1.on(); AIN2.off()
    BIN1.off(); BIN2.on()

def stop():
    AIN1.off(); AIN2.off()
    BIN1.off(); BIN2.off()

def measure_distance():
    TRIG.off()
    time.sleep_us(2)
    TRIG.on()
    time.sleep_us(10)
    TRIG.off()

    try:
        pulse = time_pulse_us(ECHO, 1, 30000)
        if pulse < 0:
            return None
        dist_cm = (pulse / 2) / 29.1
        return dist_cm
    except:
        return None
def login_page():
    return """<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
    <style>
    body {
    background-color: black;
    font-family: 'Pacifico', cursive;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    margin: 0;
}
.login-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 50px; /* to make space between login box and company name */
}
.login-box {
    background: black;
    padding: 32px;
    justify-content: center;
    border: 1px solid dimgray;
    border-radius: 10px;
    color:whitesmoke;
    box-shadow: 0 0 25px cyan;
    width: 350px;
    max-width:90%;
    /* TOGGLE EFFECT FOR LOGIN BOX */
    transition: all 0.3s ease;
    transform: scale(1);
}
.login-box:hover {
    transform: scale(1.05);
    box-shadow: 0 0 35px cyan;

}
h2 {
    text-align: center;
}
input[type="text"], input[type="password"] {
    width: 100%;
    padding: 10px;
    margin: 10px 0;
    border: 1px solid black;
    border-radius: 5px;
    font: inherit;
    box-sizing: border-box;
    background: white;
    color: black;
}
button {
    width: 100%;
    padding: 12px;
    background-color:cyan;
    color:black;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-weight: bold;
    font: inherit;
    margin-top: 16px;
}
.name {
    text-align: center;
    color: cyan;
    font-size: 1.5rem;
    line-height: 1.4;
}
.info {
    margin: 0;
    font-family: 'Share Tech Mono', monospace;
    font-size: 40px; 
    font-weight: bold;
    color: whitesmoke;
    letter-spacing: 3px; 
    text-transform: uppercase; 
}
    </style>
</head>
<body>
    <div class="login-container">
        <form class="login-box" method="POST" action="/login">
            <h2>Login</h2>
            <input type="text" name="username" placeholder="Username" required><br>
            <input type="password" name="password" placeholder="Password" required><br>
            <button type="submit">Sign In</button>
        </form>
    <div class="name">
    <h2 class="info"><strong>HANDS ON ROBOTICS</strong></h2>
    <p>By <b>RoboVITics Club</b></p>
    </div>
    </div>
</body>
</html> """

def html_page():
    return """ <!DOCTYPE html>
<html>
<head>
    <title>ESP32 Bot Control</title>
    <style>
        * {box-sizing: border-box;}

body{
  padding-top: 20px;
  font-family:Arial,sans-serif;
  background-color:black;
  display:flex;
  font-size:1.5rem;
  flex-direction:column;
  align-items:center;
  margin:0;
}
h1{
  text-align: center;
  color:cyan;
}
.button,.info{
  background-color: dimgrey;
  color:cyan;
  margin-bottom: 10px;
}
.button-container{
  display:grid;
  grid-template-columns:1fr 1fr 1fr;
  grid-template-rows:1fr 1fr 1fr;
  gap:10px;
  width:300px;
  height:300px;
  margin-bottom:30px;
}
.button{
  padding:15px 30px;
  font-size:16px;
  font-weight:bold;
  background:black;
  color: cyan;
  border:2px solid cyan;
  border-radius: 12px;
  cursor:pointer;
  display:flex;
  align-items:center;
  justify-content:center;
  text-decoration:none;
  transition:all 0.2s;
}
.button:hover{
  background-color: cyan;
  color: #000;
  box-shadow:0 6px 15px rgba(0,255,180,0.5);
  transform:translateY(-8px);
}
.button:active{transform:translateY(0);}
.center-dot{
  width:16px;
  height:16px;
  background-color:cyan;
  border-radius:50%;
  align-self:center;
  justify-self:center; 
}
.info{
  background-color: black;
  margin-top:30px;
  font-size:18px;
  padding:15px 30px;
  border-radius:8px;
  color: whitesmoke;
  border: 2px solid cyan;
}
.forward{grid-column:2;grid-row:1;}
.left{grid-column:1;grid-row:2;}
.right{grid-column:3;grid-row:2;}
.backward{grid-column:2;grid-row:3;}
.center-dot{grid-column:2;grid-row:2;}
.name{
    text-align: center;
    margin-top: 20px;
    color: cyan;
    font-size: 1.3rem;
    line-height: 1.4;
}
    </style>
    <script>
        function updateDistance() {
            fetch('/distance')
                .then(res => res.text())
                .then(data => {
                    document.getElementById("distance").innerText = data;
                });
        }
        setInterval(updateDistance, 500);
        window.onload = updateDistance;
        // Movement handling (hold button = move, release = stop)
        function sendCommand(cmd, isDown) {
            fetch(isDown ? '/' + cmd : '/stop');
        }
    </script>
</head>
<body>
    <h1>ESP32 Bot Control</h1>
<div class="button-container">
    <div class="button forward" 
         onmousedown="sendCommand('forward',true)" 
         onmouseup="sendCommand('forward',false)" 
         ontouchstart="sendCommand('forward',true)" 
         ontouchend="sendCommand('forward',false)">Forward</div>

    <div class="button left" 
         onmousedown="sendCommand('left',true)"
         onmouseup="sendCommand('left',false)" 
         ontouchstart="sendCommand('left',true)" 
         ontouchend="sendCommand('left',false)">Left</div>

    <div class="center-dot"></div>

    <div class="button right" 
         onmousedown="sendCommand('right',true)" 
         onmouseup="sendCommand('right',false)" 
         ontouchstart="sendCommand('right',true)" 
         ontouchend="sendCommand('right',false)">Right</div>

    <div class="button backward" 
         onmousedown="sendCommand('backward',true)" 
         onmouseup="sendCommand('backward',false)" 
         ontouchstart="sendCommand('backward',true)" 
         ontouchend="sendCommand('backward',false)">Backward</div>
</div>
    <div class="info" id="distance">Loading...</div>
    <div class="name">
    <h2><strong>HANDS ON ROBOTICS</strong></h2>
    <p>By <b>RoboVITics Club</b></p>
    </div>
</body>
</html> """
def handle_client(client):
    global session_authenticated
    request = client.recv(1024).decode('utf-8')
    print(request)

    method = request.split(' ')[0]
    path = request.split(' ')[1]

    if path.startswith('/login') and method == 'POST':
        body = request.split('\r\n\r\n')[-1]
        data = {}
        for pair in body.split('&'):
            if '=' in pair:
                key, value = pair.split('=')
                data[key] = value

        username = data.get("username", "")
        password = data.get("password", "")

        if username == USERNAME and password == PASSWORD_AUTH:
            session_authenticated = True
            client.send('HTTP/1.1 302 Found\r\nLocation: /\r\n\r\n')
        else:
            session_authenticated = False
            client.send('HTTP/1.1 401 Unauthorized\r\n\r\n<h1>Unauthorized</h1>')
        client.close()
        return

    if not session_authenticated and path != "/login":
        client.send('HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n')
        client.send(login_page())
        client.close()
        return

    # Real-time distance AJAX call
    if path == "/distance":
        dist = measure_distance()
        if dist is None or dist > 100:
            msg = "No Obstacle Detected"
        else:
            msg = f"Obstacle Ahead: {dist:.2f} cm"
        client.send('HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\n')
        client.send(msg)
        client.close()
        return

    # Bot movement control
    if path == "/forward":
        move_forward()
    elif path == "/backward":
        move_backward()
    elif path == "/left":
        move_left()
    elif path == "/right":
        move_right()
    elif path == "/stop":
        stop()
    else:
    # Default = stop (safety)
        stop()

    # Main control UI
    client.send('HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n')
    client.send(html_page())
    client.close()

# Server setup
ip = connect_wifi()
addr = socket.getaddrinfo(ip, 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)
print("Listening on", addr)

while True:
    try:
        client, addr = s.accept()
        handle_client(client)
    except Exception as e:
        print("Error:", e)
