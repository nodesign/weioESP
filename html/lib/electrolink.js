(function(window){
    'use strict';
    function define_Electrolink(){
        var Electrolink = {};

        /**
        * Server address to connect to 
        */
        var BROKER_ADDRESS = "ws://78.194.220.232:4444";
        var REQUEST_TOPIC = "weio_command";
        var ANSWER_TOPIC = "weio_reply";
        var ERROR_TOPIC = "weio_error";

        /**
         * Define callbacks here and request keys
         * Each key is binded to coresponding function
         */
        var weioCallbacks = {};

        var client = mqtt.connect(BROKER_ADDRESS); // you add a ws:// url here

        client.subscribe(ANSWER_TOPIC);
        client.subscribe(ERROR_TOPIC);

        //console.log(new Date().getTime());

        client.on("message", function (topic, payload) {
            var data = JSON.parse(payload);
            if (topic == ANSWER_TOPIC) {

                var instruction = data.value[1];
                if (instruction in weioCallbacks) {
                    weioCallbacks[instruction](data.value);
                }

                } else if (topic == ERROR_TOPIC) {
                    var err = JSON.parse(payload);
                    console.log("ERROR",err);
                }
                //client.end();
            });

        Electrolink.OUT = 0;
        Electrolink.IN  = 1;
        Electrolink.PULL_UP = 2;
        Electrolink.PULL_DOWN = 3;

        // PWM
        Electrolink.pwmStart = function(pwmNb, frequence) {
            Electrolink.sender("pwmStart", [pwmNb, frequence]);
        }

        Electrolink.pwmSet = function(pwmNb, duty) {
            Electrolink.sender("pwmSet", [pwmNb, duty]);
        }

        Electrolink.pwmStop = function(pwmNb) {
            Electrolink.sender("pwmStop", [pwmNb]);
        }

        // DIGITAL GPIO

        Electrolink.pinMode = function(pinId, mode) {
            Electrolink.sender("pinMode", [pinId, mode]);
        }

        Electrolink.digitalWrite = function(pinId, value) {
            Electrolink.sender("digitalWrite", [pinId, value]);
        }

        Electrolink.digitalRead = function(pinId, callback) {
            // create UUID for this callback function and store it
            // in array
            var cbId = uuid.v4();
            //console.log("callback name:" + fName);
            weioCallbacks[cbId] = callback
            // pass callback uuid to match it with answer
            // uuid will be returned with answer
            // in that way it's possible to define multiple
            // digitalReads with different callbacks
            Electrolink.sender("digitalRead", [pinId, cbId]); 
        }

        Electrolink.sender = function(method, params) {
            var data = {"method":method, "params":params};
            client.publish(REQUEST_TOPIC, JSON.stringify(data));
        }
        
        
        return Electrolink;
    }
    //define globally if it doesn't already exist
    if(typeof(Electrolink) === 'undefined'){
        window.Electrolink = define_Electrolink();
    }
    else{
        console.log("Electrolink library already defined!");
    }
})(window);

