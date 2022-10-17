const input_name = document.getElementById('id_nome')

input_name.addEventListener('keypress', function (e) {
    if (!checkChar2(e)){
        e.preventDefault()
    }
})



function checkChar2(e) {
    const char = String.fromCharCode(e.keyCode);

    const pattern = '[a-zA-Z]'

    if(char.match(pattern)) {
        return true
    }
}