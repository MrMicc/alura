/**
 * Created by luizmiccieli on 30/10/16.
 */

var botao = document.getElementById('calcula-imcs');

botao.addEventListener('click', function () { //função responsável em calcular os IMCs
    var pacientes = getPacientes('paciente');

    for(i=0;i<pacientes.length;i++){
        console.log('Nome: '+paciente[i].nome
            +' Altura: '+paciente[i].altura
            +' Peso: '+paciente[i].peso
            +' IMC: '+paciente[i].imc()
        );
    }
});

function calculaImc(){

}




