var slider;
var sY;
var sliderPosY;
var initSliderPosY;
var maxUp, maxDown;

var percent = 50;
var p_percent;

function setup() {

    createCanvas(windowWidth, windowHeight);
    // always put some frame rate, don't make suffer cpu or websockets
    frameRate(12);
    slider = loadImage("warmCold.png");
    imageMode(CENTER);

    sliderPosY = height/2.0;
    initSliderPosY = sliderPosY;
    textFont("Helvetica");
    textSize(18);
    
}

function draw() {
    background(0);

    image(slider,width/2.0, sliderPosY);
    
    percent = parseInt(map(sliderPosY, height/2.0 + slider.height/2.0-20, height/2.0 - slider.height/2.0+20, 100,0));
    noStroke();
    
    var kelvin = parseInt(map(sliderPosY, height/2.0 + slider.height/2.0-20, height/2.0 - slider.height/2.0+20, 2700, 6500));
    var colorIter = map(percent, 100,0, 0,1);
    var txtColor = lerpColor(color(253,222,123), color(149,231,253), colorIter);
    fill(txtColor);
    text(kelvin + " K", 10, height/2.0-10);
    
    stroke(255);
    line(0,height/2.0, width, height/2.0);
    //noLoop();
    //fill(149,231,253);
    //text(100-percent, 30, height/2.0+60);
}

function touchMoved() {
    sliderPosY = initSliderPosY+(mouseY-sY);

    if (sliderPosY > height/2.0 + slider.height/2.0-20) sliderPosY = height/2.0 + slider.height/2.0-20;
    if (sliderPosY < height/2.0 - slider.height/2.0+20) sliderPosY = height/2.0 - slider.height/2.0+20;
    
    if (abs(percent - p_percent) > 5) {
        Electrolink.sender("percentColor",[percent]);
        console.log("sending", percent);
    }
    p_percent = percent;
    //redraw();
    return false;
}


function touchStarted() {
    sY = mouseY;
}

function touchEnded() {
    initSliderPosY = sliderPosY;
}