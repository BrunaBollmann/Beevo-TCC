 const input = document.getElementById('id_matricula')

input.addEventListener('keypress', function (e) {
    if (!checkChar(e)){
        e.preventDefault()
    }

})

function checkChar(e) {
    const char = String.fromCharCode(e.keyCode);

    const pattern = '[0-9]'

    if(char.match(pattern)) {
        console.log(char)
        return true
    }
}
