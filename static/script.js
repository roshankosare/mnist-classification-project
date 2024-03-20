var canvas = document.getElementById("myCanvas");
var ctx = canvas.getContext("2d");
var isDrawing = false;

canvas.addEventListener("mousedown", startDrawing);
canvas.addEventListener("mousemove", draw);
canvas.addEventListener("mouseup", endDrawing);
canvas.addEventListener("mouseout", endDrawing);

function startDrawing(event) {
    isDrawing = true;
    draw(event);
}

function draw(event) {
    if (!isDrawing) return;
    var x = event.clientX - canvas.getBoundingClientRect().left;
    var y = event.clientY - canvas.getBoundingClientRect().top;
    ctx.strokeStyle = "#FFFFFF"; // Set drawing color to white
    ctx.lineCap = "round";
    ctx.lineWidth = 10;
    ctx.lineTo(x, y);
    ctx.stroke();
    ctx.beginPath();
    ctx.moveTo(x, y);
}

function endDrawing() {
    isDrawing = false;
    ctx.beginPath();
}

function sendImage() {
    var imageData = canvas.toDataURL("image/png"); // Convert canvas to base64 image data
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/");
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText); // Parse the JSON response
            displayPrediction(response.prediction); // Call a function to display the prediction
        }
    };
    xhr.send(JSON.stringify({ imageData: imageData })); // Send the image data
}

function displayPrediction(prediction) {
    var predictionElement = document.getElementById("prediction"); // Get the element where prediction will be displayed
    predictionElement.innerText = "Prediction: " + prediction; // Set the text content to show the prediction
}

function clearCanvas() {
    displayPrediction("")
    ctx.clearRect(0, 0, canvas.width, canvas.height); // Clear the canvas
}