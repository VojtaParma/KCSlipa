let grid = document.getElementById("grid");
let barva = "white";

let text = document.createElement("h2");
text.innerText = "Mode: white";

document.body.appendChild(text);

document.onkeydown = function(event) {

    if (event.key == "o") {
        barva = "orange";
        text.innerText = "Mode: orange";
    }

    if (event.key == "b") {
        barva = "blue";
        text.innerText = "Mode: blue";
    }

    if (event.key == "r") {
        barva = "red";
        text.innerText = "Mode: red";
    }
    if (event.key == "g") {
        barva = "green";
        text.innerText = "Mode: green";
    }
    if (event.key == "w") {
        barva = "white";
        text.innerText = "Mode: white";
    }

};

// načtení uložených dat
let ulozeneBarvy = JSON.parse(localStorage.getItem("grid")) || [];

for (let i = 0; i < 100; i++) {

    let box = document.createElement("div");

    box.classList.add("box");

    // načte uloženou barvu
    if (ulozeneBarvy[i]) {
        box.style.backgroundColor = ulozeneBarvy[i];
    }

    box.onclick = function() {

        box.style.backgroundColor = barva;

        // uloží barvu
        ulozeneBarvy[i] = barva;

        localStorage.setItem("grid", JSON.stringify(ulozeneBarvy));
    };

    grid.appendChild(box);
}