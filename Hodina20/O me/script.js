function prepniRezim() {
    document.body.classList.toggle("dark");
}

function pridej() {
    let text = document.getElementById("input").value;

    if (text === "") return;

    let div = document.createElement("div");

    let p = document.createElement("p");
    p.innerText = text;
    p.style.display = "inline";

    let btn = document.createElement("button");
    btn.innerText = "Smazat";
    btn.onclick = function() {
        div.remove();
    };

    div.appendChild(p);
    div.appendChild(btn);

    document.getElementById("seznam").appendChild(div);

    document.getElementById("input").value = "";
}