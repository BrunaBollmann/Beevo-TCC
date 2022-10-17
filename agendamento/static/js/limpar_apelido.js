const input_apelido = document.getElementById('id_apelido')

input_apelido.addEventListener('keypress', function (e) {
    if (!checkChar2(e)){
        e.preventDefault()
    }
})