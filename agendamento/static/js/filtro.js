function retira_acentos(str) {
	com_acento = "ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝŔÞßàáâãäåæçèéêëìíîïðñòóôõöøùúûüýþÿŕ";
	sem_acento = "AAAAAAACEEEEIIIIDNOOOOOOUUUUYRsBaaaaaaaceeeeiiiionoooooouuuuybyr";
	novastr = "";
	for (i = 0; i < str.length; i++) {
		troca = false;
		for (a = 0; a < com_acento.length; a++) {
			if (str.substr(i, 1) == com_acento.substr(a, 1)) {
				novastr += sem_acento.substr(a, 1);
				troca = true;
				break;
			}
		}
		if (troca == false) {
			novastr += str.substr(i, 1);
		}
	}
	return novastr;
}
var filtro = document.getElementById('filtro-input');
var tabela = document.getElementById('tabela');
filtro.onkeyup = function () {
	var nomeFiltro = retira_acentos(filtro.value.toLowerCase());
	for (var i = 1; i < tabela.rows.length; i++) {
		var conteudoCelula = retira_acentos(tabela.rows[i].cells[3].innerText);
		var corresponde = conteudoCelula.toLowerCase().indexOf(nomeFiltro) >= 0;
		tabela.rows[i].style.display = corresponde ? '' : 'none';
	}
};