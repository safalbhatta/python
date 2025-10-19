let bgcolor;
let lastColorChange = 0;

function setup() {
    createCanvas(1000, 1000);
    bgcolor = color(220); // Initialize bgcolor
    background(bgcolor);
}

function draw() {
    background(bgcolor); // Corrected function name
    if (keyIsDown(82)) { // Corrected function name
        if (millis() - 500 > lastColorChange) { // Corrected variable name
            bgcolor = color(random(0, 255), random(0, 255), random(0, 255)); // Corrected function usage
            lastColorChange = millis(); // Corrected variable name

        }
    }
    stroke(0, 126, 204);
    strokeWeight(8);
    noFill();
    ellipse(55, 55, 100, 100); // Draw a circle at the center with a diameter of 100
    stroke(249, 172, 49);
    ellipse(110, 110, 100, 100); // Draw another circle
    stroke(0,0,0); // Corrected function name
    ellipse(165, 55, 100, 100); // Draw another circle
    stroke(0,159,61);
    ellipse(220, 110, 100, 100); // Draw another circle
    stroke(223,0,36);
    ellipse(275, 55, 100, 100); // Draw another circle
 
}

