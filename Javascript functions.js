function testfunction() {
    console.log("test");
}
score = 0;
clickmex = 0;
addpersec = 0;

// Functions for java dump
function clickme() {
    clickmex++;
    document.getElementById("clickmeoutput").innerText = clickmex;
}
function donttouch() {
    document.getElementById("handhold").innerHTML = "Dont touch me...";
    setTimeout(holdyourhand, 2500); // Wait 2.5 seconds before changing the text
}
function holdyourhand() {
    document.getElementById("handhold").innerHTML = "I'm gonna hold your hand when I say this.";
}
// Functions for clicker game structure
function clickergameaddscore(amount) {
    score += amount;
    document.getElementById("clickergameaddscore").innerText = "You score is: " + Number.parseFloat(score.toFixed(9)); // Update the button text with the score
}
function clickergametimesscore(amount) {
    score *= amount;
    document.getElementById("clickergameaddscore").innerText = "You score is: " + Number.parseFloat(score.toFixed(9)); // Update the button text with the score
}
function clickergameaddscorepersec(amount) {
    addpersec += amount;
    document.getElementById("clickergamescorepersec").innerText = Number.parseFloat(addpersec.toFixed(9)) + "/sec"; // Update the button text with the score per second
}
function mainintervalfunc() {
    maininterval = setInterval(function () {clickergameaddscore(addpersec)}, 1000); //adds the current per second rate})
}
// Function for clicker game upgrades
function AutomaticClicker() {
    if (score >= 10) {
        clickergameaddscore(-10); // Deduct 10 points for the auto clicker
        clickergameaddscorepersec(0.1) // Click every second
    }
    else {
        alert("You don't have enough points for the auto clicker! You need at least 10 points.");
        return;
    }
}
function RoundingError() {
    if (score >= 150) {
        clickergameaddscore(-150); // Deduct 150 points for the rounding error
        clickergametimesscore(1.1); // Multiply score by 1.1
    }
    else {
        alert("You don't have enough points for the Rounding Error! You need at least 150 points.");
        return;
    }
}

// Function to run when the page loads
function onloadfuncs() {
    mainintervalfunc(); // Start the main interval function when the page loads
}