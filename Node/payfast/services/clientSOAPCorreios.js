/**
 * Created by luizmiccieli on 21/11/16.
 */
var soap = require('soap');


function ClientSOAPCorreios() {
    this._url = 'http://ws.correios.com.br/calculador/CalcPrecoPrazo.asmx?wsdl';
}

ClientSOAPCorreios.prototype.calculaPrazo = function (dadosEntrega, callback) {
    var jsonPackage = {'nCdServico' : dadosEntrega.codServico, 'sCepOrigem' : dadosEntrega.cepOrigem, 'sCepDestino' : dadosEntrega.cepDestino};
    //criando um cliente nos correios
    soap.createClient(this._url, function (error, client) {
        console.log('Preparando para enviar requisicao ao correios');
        //chamando o calculo de prazo nos correios passando o callback da origem
        client.CalcPrazo(jsonPackage,callback);
    });
};


module.exports = function () {
    return ClientSOAPCorreios;
};

