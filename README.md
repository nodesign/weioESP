# WeIO ESP

This is experimental project that is a proof of concept for Electrolink and WeIO architecture. Work is still in progress
## Installation

##Mqtt broker
On your pc or on rPi install and launch broker
```bash
npm install aedes --save
node broker.js
```
This will launch mqtt broker on two ports, mqtt protocol and websocket protocol
Remember your ip address because you will need it

## Http server
Launch some http server and point to html directory. I'm using lighttpd on rPi that works just fine
Fix your mqtt broker server ip address in file html/lib/electrolink.js
```javascript
var BROKER_ADDRESS = "ws://XXX.XXX.XXX.XXX:8888";
```
## Micropython sources
Fix your mqtt broker server ip address in file micropythonElectrolink/elServer.py
```python
server="XXX.XXX.XXX.XXX"
```
Upload files from micropythonElectrolink to your ESP board using ampy tool
```bash
ampy -p /dev/tty.wchusbserial1410 put micropythonElectrolink/electrolink.py
ampy -p /dev/tty.wchusbserial1410 put micropythonElectrolink/elServer.py
```

Enter in ESP board using serial console (screen, minicom,...)
```bash
screen /dev/tty.wchusbserial1410 115200
```
Now launch Electrolink server
```bash
import elServer
elServer.start()
```

## Run 
Make sure that you ran mqtt broker server at first and then micropython Electrolink server.
Type your http server ip address in browser and enjoy

## License 
[BSD](https://opensource.org/licenses/BSD-3-Clause)