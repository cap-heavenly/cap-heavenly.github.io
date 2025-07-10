
function testfunction() {
    console.log("test");
}

let clickmex = 0;
let sebsize = 1;


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
function seb(mode, x) {
    if (mode == "grow") {
        console.log("activated")
        if (parseInt(x.style.width, 10) <= 500) {
            sebsize += 0.001;
            sebwidth = parseInt(x.style.width,10) + sebsize;
            sebheight = parseInt(x.style.height,10) + sebsize;
            x.style.width = sebwidth + "px";
            x.style.height = sebheight + "px";
            console.log("sebwidth: " + sebwidth + " sebheight: " + sebheight);
            console.log(x.style.width + " " + x.style.height);
        }
        else {
            x.src = "Assets/sebby.png";
        }
    }
    else {
        x.style.width = 50 + "px";
        x.style.height = 65 + "px";
        x.src = "Assets/sebby.jpg";
    }
}


function formtofile(form, file) {
    open(file, "a", (err) => {
        if (err) throw err;
        text = "";
        for (i=0; i<form.length; i++){text += x.elements[i].value + "\n"}
        appendFile(text);
    })
}
function testing() {
    appendFile("Formsubs/favouritetvshow.txt", "test", utf8);
}
// Function to run when the page loads
function onloadfuncs() {
    mainintervalfunc(); // Start the main interval function when the page loads
}