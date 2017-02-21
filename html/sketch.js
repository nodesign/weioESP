var h = 600;
var light = 0;
var state = false;
var mycolor;

function setup() {
    // Electrolink.pwmStart(5,255);
    // Electrolink.pinMode(0, Electrolink.IN);
    //
    // Electrolink.digitalRead(0,  function readCallback(data) {
    
    //    console.log("read from pin",data);

    //});

    
    // canvas size in pixels
    createCanvas(windowWidth, windowHeight);
    // always put some frame rate, don't make suffer cpu or websockets
    frameRate(12);
//    console.log(Please.make_color());


    setInterval(function(){
        myColor = Please.make_color();
        var l = Math.floor((Math.random() * 21) + 1);

        if (state) {
            Electrolink.sender("fadeinTube", [40, myColor]);
        } else {
            Electrolink.sender("fadeoutTube", [20]);
        }
        state = !state;
        // Electrolink.sender("setTubeColorAll",["#000000"]);
        // for (var i=0; i<l; i++) {
        //     Electrolink.sender("setTubeColor",[21-i, myColor]);
        //     Electrolink.sender("setTubeColor",[20+i, myColor]);
        // }

        Electrolink.sender("writeColors",[""]);
        console.log("sending", myColor);
    }, 3000);
    
}

function draw() {
    background(0);
    
    var p = map(h, 60, height-60, 80,1);
    
    if (h<60) h = 60;
    if (h>height-60) h = height-60;

    fill(myColor);
    ellipse(width/2.0, height/2.0, p, height);
    light = parseInt(map(h, 60, height-60, 1023,0));


}

function touchMoved() {
  h = mouseY;
  Electrolink.sender("lighting",[light]);
  //Electrolink.pwmSet(5,light);
  // prevent default
  return false;
}