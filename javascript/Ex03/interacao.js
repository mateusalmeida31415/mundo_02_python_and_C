var pInicio = document.querySelector('input#txtini')
var pFim = document.querySelector('input#txtfim')
var pPasso = document.querySelector('input#txtpasso')
var botao = document.querySelector('input#btn')
var result = document.querySelector('p#exibir')  

botao.addEventListener('click', clicar)

function clicar(){
    var ini = Number(pInicio.value)
    var fim = Number(pFim.value)
    var passo = Number(pPasso.value)

    if(ini == 0 || fim == 0 || passo == 0){
        window.alert("Erro! Há algum valor inválido!")
    }else{
        result.innerHTML = 'Contando: <br>'
        if(fim > ini){
            for(let c = ini; c <= fim; c += passo){
            result.innerText += ` ${c} \u{1F449}`
            }
        }else{
            for(let c = ini; c >= fim; c -= passo){
                result.innerText += ` ${c} \u{1F449}`
            }
        }
    result.innerText += `\u{1F6A9}`
    }
}
