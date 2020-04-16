var numCampo = document.querySelector('input#txtn') 
var botao = document.querySelector('input#btn')
var botaoClean = document.querySelector('input#btnClean')
var result = document.querySelector('p#res')

botao.addEventListener('click', clicar)
botaoClean.addEventListener('click', limpar)

function clicar(){
    let num = Number(numCampo.value)
    result.innerHTML = `A Tabuada de ${num} é: <br><br>`
    for(let i = 0; i <= 10; i++){
        result.innerHTML += `${num} x ${i} = ${num*i} <br>`
    }

}

function limpar(){
    result.innerHTML = " "
}