var diameterX = 30;
var diameterY = 30;

var selectorX;
var selectorY;

var state = true;
var cnt = 0;
var amt = 10;
var step = 1;

var touchedY = false;
var touchedX = false;

function setup() {

    createCanvas(windowWidth, windowHeight);
    // always put some frame rate, don't make suffer cpu or websockets
    frameRate(12);
    selectorY = height/2.0-30;
    selectorX = width/2.0+30;
}

function draw() {
    background(0);



    if (state) {
        if (cnt < amt) 
            cnt+=step;
         else 
             state = !state
    } else {
        if (cnt > 0)
            cnt-=step;
        else 
            state = !state;
    }

    if (diameterX < 30) diameterX = 30;
    if (diameterX > 350) diameterX = 350;

    if (diameterY < 30) diameterY = 30;
    if (diameterY > 350) diameterY = 350;


    if (touchedY) {
        var a = mouseY;
        a = (a > height/2.0-30) ? height/2.0-30 : a;
        a = (a < 28) ? 28 : a;
 
        diameterY = map(a, 180, 28, 0,300);
        selectorY = a;
        //console.log(mouseY);
    }
    
    if (touchedX) {
        var a = mouseX;
        console.log(mouseX);
        // a = (a > 180) ? 180 : a;
        a = (a < 740) ? 28 : a;
//
//         diameterY = map(a, 180, 28, 0,300);
//selectorY = a;
    }
    
    fill(255);
    ellipse(width/2.0, height/2.0, selectorX/2-30, diameterY+cnt);
    
    
    fill(255,255,0);
    ellipse(width/2.0, selectorY, 20,20);
    
    fill(255,255,0);
    ellipse(selectorX, height/2.0, 20,20);

/*
    fill(255,0,0);
    ellipse(width/2.0+diameterX, height/2.0, 20,20);
*/

}

function touchMoved() {
    /*
    var dY = dist(width/2.0, height/2.0-diameterY, mouseX, mouseY);
    if (dY<10) {
        diameterY = dY*2.0;
    }
    */
    
    /*
    var d = dist(mouseX, mouseY, width/2.0, height/2.0);
    diameterX = d*2.0;
    
    amt = map(d, 0, 350, 10,60);
    step = map(d, 0,350, 1, 10);
    */
  return false;
}


function touchStarted() {
    var dY = dist(width/2.0, selectorY, mouseX, mouseY);
    if (dY<10)
        touchedY = true;
    
    var dX = dist(selectorX, height/2.0, mouseX, mouseY);
    if (dX<10)
        touchedX = true;
}

function touchEnded() {
    if (touchedY == true) touchedY = false;
    if (touchedX == true) touchedX = false;
}