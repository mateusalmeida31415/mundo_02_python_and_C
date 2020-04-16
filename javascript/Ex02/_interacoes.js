var botao = document.getElementById('btn')
botao.addEventListener('click', clicar)

function clicar(){
    var texto = document.getElementById('txt')
    var ano = new Date()
    var idade = ano.getFullYear() - Number(texto.value)
    if(idade <= 0 || idade > 150){
       window.alert('Erro! Ano inválido.')
    }else{
        var sex = document.getElementsByName('sexbt')
        var result = document.getElementById('res')
        var img = document.getElementById('fotos')
        if(sex[0].checked){
            var genero = 'Masculino'
            result.innerText = `${genero} e ${idade} anos. `
            if(idade >= 0 && idade <= 10){ 
                img.display = 'block'
            }else if(idade > 10 && idade <= 21){
                //adolecente
            }else if(idade > 21 && idade <= 50){
                //Adulto
            }else{
                //idoso
            }
        }else if(sex[1].checked){
            var genero = 'Feminino'
        }
    }
}