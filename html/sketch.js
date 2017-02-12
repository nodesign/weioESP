var h = 600;
var light = 0;

function setup() {
    pwmStart(5,255);
    pinMode(0, IN);
    digitalRead(0, read);
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

    ellipse(100,100, 40,40);


}

function touchMoved() {
  h = mouseY;
  pwmSet(5,light);
  // prevent default
  return false;
}

function read(data) {
    console.log("read",data);
}