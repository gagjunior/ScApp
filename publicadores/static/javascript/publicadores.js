let dataAtual = new Date()
let dia = dataAtual.getDate()
let mes = dataAtual.getMonth() + 1
let ano = dataAtual.getFullYear()

let dataFormatada = `${dia}/${mes}/${ano}`

document.getElementById('data-atual').innerText = dataFormatada

var currentImgIndex=0
var igmSrcArray = [
    "/static/imagens/seta_cima.png",
    "/static/imagens/seta_baixo.png"    
]

function alteraImagem(){
    if(currentImgIndex == igmSrcArray.length){
        currentImgIndex=0
    }
    document.getElementById("order").src=igmSrcArray[currentImgIndex]
    currentImgIndex++
    
}

