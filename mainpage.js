
function testfunction() {
    console.log("test");
}

let clickmex = 0;
let gendersize = 1;



// Functions for java dump
function clickme() {
    clickmex++;
    document.getElementById("clickmeoutput").innerText = clickmex;
}
function holdyourhand() {
    document.getElementById("handhold").innerHTML = "I'm gonna hold your hand when I say this.";
}
function donttouch() {
    document.getElementById("handhold").innerHTML = "Dont touch me...";
    setTimeout(holdyourhand, 2500); // Wait 2.5 seconds before changing the text
}



// Function for growing image
function gender(mode, x) {
    if (mode == "grow") {
        console.log("activated")
        if (parseInt(x.style.width, 10) <= 250) {
            gendersize += 0.001;
            genderwidth = parseInt(x.style.width,10) + gendersize;
            genderheight = parseInt(x.style.height,10) + gendersize;
            x.style.width = genderwidth + "px";
            x.style.height = genderheight + "px";
            console.log("genderwidth: " + genderwidth + " genderheight: " + genderheight);
            console.log(x.style.width + "   " + x.style.height);
        }
        else {
            x.src = "Assets/blowup.png";
        }
    }
    else {
        x.style.width = 65 + "px";
        x.style.height = 36 + "px";
        x.src = "Assets/nicegender.png";
    }
}




// Function to run when the page loads
function onloadfuncs() {
    mainintervalfunc(); // Start the main interval function when the page loads
}