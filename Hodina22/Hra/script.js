let grid = document.getElementById("grid");

for (let i = 0; i < 100; i++) {

    let box = document.createElement("div");

    box.classList.add("box");

    box.onclick = function() {

        let r = Math.floor(Math.random() * 256);
        let g = Math.floor(Math.random() * 256);
        let b = Math.floor(Math.random() * 256);

        box.style.backgroundColor =
            "rgb(" + r + "," + g + "," + b + ")";
    };

    grid.appendChild(box);
}