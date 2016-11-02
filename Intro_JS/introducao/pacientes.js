
/**
 * Created by luizmiccieli on 30/10/16.
 */

function getPacientes(element){
    var trPacientes = document.getElementsByClassName(element);

    var pacientes;
    for(i=0; i<trPacientes.length;i++){
        pacientes = montaPaciente(trPacientes[i]);
    }
    return (trPacientes,pacientes);
}

function montaPaciente(trPaciente) {
    var tdNome = trPaciente.getElementsByClassName('info-nome')[0];
    var tdPeso = trPaciente.getElementsByClassName('info-peso')[0];
    var tdAltura = trPaciente.getElementsByClassName('info-altura')[0];


    var paciente = {
        nome : tdNome.textContent,
        peso : tdPeso.textContent,
        altura : tdAltura.textContent,
        imc : function(){
            if(this.peso !=0  &&  this.altura !=0) {
                return this.peso / (this.altura * this.altura);
            }else{
                console.log('peso ou altura não podem ser iguais a zero!!!')
            }
        }
    }
    setTDIMC(trPaciente,paciente);
    return paciente;

}

function setTDIMC(trPaciente, paciente) {
    var tdImc = trPaciente.getElementsByClassName('info-imc')[0];
    tdImc.textContent = paciente.imc();

}
