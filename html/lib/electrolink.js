var BROKER_ADDRESS = "ws://78.194.220.232:8888";
var REQUEST_TOPIC = "weio_command";
var ANSWER_TOPIC = "weio_reply";
var ERROR_TOPIC = "weio_error";

var OUT = 0;
var IN  = 1;
var PULL_UP = 2;
var PULL_DOWN = 3;

/**
 * Define callbacks here and request keys
 * Each key is binded to coresponding function
 */
var weioCallbacks = {};


var client = mqtt.connect(BROKER_ADDRESS); // you add a ws:// url here

client.subscribe(ANSWER_TOPIC);
client.subscribe(ERROR_TOPIC);

client.on("message", function (topic, payload) {
    var data = JSON.parse(payload);
    if (topic == ANSWER_TOPIC) {

        instruction = data.value[1];
        if (instruction in weioCallbacks) {
            weioCallbacks[instruction](data.value);
        }

        } else if (topic == ERROR_TOPIC) {
            var err = JSON.parse(payload);
            console.log("ERROR",err);
        }
        //client.end();
    });

// PWM
function pwmStart(pwmNb, frequence) {
    sender("pwmStart", [pwmNb, frequence]);
}

function pwmSet(pwmNb, duty) {
    sender("pwmSet", [pwmNb, duty]);
}

function pwmStop(pwmNb) {
    sender("pwmStop", [pwmNb]);
}

// DIGITAL GPIO

function pinMode(pinId, mode) {
    sender("pinMode", [pinId, mode]);
}

function digitalWrite(pinId, value) {
    sender("digitalWrite", [pinId, value]);
}

function digitalRead(pinId, callback) {
    // create new callback call
    var fName = callback.name;
    //console.log("callback name:" + fName);
    weioCallbacks[fName] = callback
    // pass callback name to match it with answer
    // callback name will be returned with answer
    // in that way it's possible to define multiple
    // digitalReads with different callbacks
    sender("digitalRead", [pinId, fName]); 
}

function sender(method, params) {
    data = {"method":method, "params":params};
    client.publish(REQUEST_TOPIC, JSON.stringify(data));
}
