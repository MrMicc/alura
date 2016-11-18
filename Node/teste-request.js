/**
 * Created by luizmiccieli on 07/11/16.
 */

var http = require('http');

var config = {
    hostname : 'localhost',
    port : 3000,
    path : '/produtos',
    headers : {
        'Accept' : 'application/json'
    }
};


/**
 * Retorna o Json do proveninete do controller
 */
http.get(config, function (res) { //fazendo uma requisição no servidor
    console.log(res.statusCode);
    res.on('data', function (body) {
        console.log('Result : \n'+body); //imprimindo o resultado
    })

});