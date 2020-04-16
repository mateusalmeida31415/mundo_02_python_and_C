var b = window.document.body
document.addEventListener('DOMContentLoaded', reload)
function reload(){
    var horas = new Date()
    var p = window.document.querySelector('p#mhora')
    var f = document.querySelector('img#fotos')
   
    if(horas.getHours() >= 1 && horas.getHours() < 12){
        p.innerHTML = `Agora são ${horas.getHours().toFixed(2).replace('.',':')}.`
        b.style.background = 'lightgreen'
        f.src = 'manha.jpg'
    }
    
    if(horas.getHours() >= 12 && horas.getHours() < 18){
        p.innerHTML = `Agora são ${horas.getHours().toFixed(2).replace('.',':')}.`
        b.style.background = 'orange'
        f.src = 'tarde.jpg'
    }

    if(horas.getHours() >= 18 && horas.getHours() < 24){
        p.innerHTML = `Agora são ${horas.getHours().toFixed(2).replace('.',':')}.`
        b.style.background = 'grey'
        f.src = 'noite.jpg'
    }
}