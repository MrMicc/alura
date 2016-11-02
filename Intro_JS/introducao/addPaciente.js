/**
 * Created by luizmiccieli on 02/11/16.
 */

var botaoAddPaciente = document.getElementById('adicionar-paciente');

botaoAddPaciente.addEventListener('click',function(event) {

    event.preventDefault();

    paciente = mountPacienteFromForm();
    addTabela(paciente);

});

function addTabela(paciente){
    var tabela = document.getElementById('tabela-pacientes');
    var novoPaciente = '<tr class="paciente">'+
        '<td class="info-nome">'+paciente.nome+'</td>'+
        '<td class="info-peso" id="peso-2">'+paciente.peso +'</td>'+
        '<td class="info-altura" id="altura-2">'+paciente.altura+'</td>'+
        '<td class="info-imc" id="imc-2">'+paciente.imc()+'</td>'+
        '</tr>';

    tabela.innerHTML = tabela.innerHTML + novoPaciente;

    limpandoForm();


}

function limpandoForm() {
    document.getElementById('campo-nome').value = '';
    document.getElementById('campo-peso').value = '';
    document.getElementById('campo-altura').value = '';

}

function mountPacienteFromForm() {
    paciente = {
        nome : document.getElementById('campo-nome').value,
        peso : document.getElementById('campo-peso').value,
        altura: document.getElementById('campo-altura').value,
        imc : function(){
            if(this.peso !=0  &&  this.altura !=0) {
                return this.peso / (this.altura * this.altura);
            }else{
                console.log('peso ou altura não podem ser iguais a zero!!!')
            }
        },
    };

    return paciente;

}