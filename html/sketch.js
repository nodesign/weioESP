var h = 600;
var light = 0;

function setup() {
    Electrolink.pwmStart(5,255);
    Electrolink.pinMode(0, Electrolink.IN);
    
    Electrolink.digitalRead(0,  function readCallback(data) {

        console.log("read from pin",data);

    });
    // canvas size in pixels
    createCanvas(windowWidth, windowHeight);
    // always put some frame rate, don't make suffer cpu or websockets
    frameRate(12);
}

function draw() {
    background(255);
    
    var p = map(h, 60, height-60, 80,1);
    
    if (h<60) h = 60;
    if (h>height-60) h = height-60;

    fill(0);
    ellipse(width/2.0, height/2.0, p, height);
    light = parseInt(map(h, 60, height-60, 255,0));


}

function touchMoved() {
  h = mouseY;
  Electrolink.pwmSet(5,light);
  // prevent default
  return false;
}