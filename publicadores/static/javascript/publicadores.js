let dataAtual = new Date()
let dia = dataAtual.getDate()
let mes = dataAtual.getMonth() + 1
let ano = dataAtual.getFullYear()

let dataFormatada = `${dia}/${mes}/${ano}`

document.getElementById('data-atual').innerText = dataFormatada

function w3_open() {
    document.getElementById("mySidebar").style.display = "block";
}
  
function w3_close() {
    document.getElementById("mySidebar").style.display = "none";
}