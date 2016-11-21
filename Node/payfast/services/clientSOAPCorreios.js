/**
 * Created by luizmiccieli on 21/11/16.
 */
var soap = require('soap');

soap.createClient('http://ws.correios.com.br/calculador/CalcPrecoPrazo.asmx?wsdl',
    function(error, client){
        console.log('client soap criado :)');
        client.CalcPrazo({'nCdServico' : '40010', 'sCepOrigem' : '71535030', 'sCepDestino' : '65000600'}, function (err, result) {
            console.log('ERRO:: '+err);
            console.log('RESULTADO::  '+JSON.stringify(result));
        })
});
