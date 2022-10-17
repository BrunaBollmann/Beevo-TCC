const input_sobrenome = document.getElementById('id_sobrenome')

input_sobrenome.addEventListener('keypress', function (e) {
    if (!checkChar2(e)){
        e.preventDefault()
    }
})