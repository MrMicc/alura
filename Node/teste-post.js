/**
 * Created by luizmiccieli on 07/11/16.
 */

var http = require('http');

var config = {
    hostname : 'localhost',
    port : 3000,
    path : '/produtos',
    method : 'post', //informando o metodo a ser utilizado para realziar a inserção
    headers : {
        'Accept' : 'application/json',
        'Content-type': 'application/json'
    }
};


/**
 * abre um requst no client
 */
var request = http.request(config, function (res) { //fazendo uma requisição no servidor
    console.log(res.statusCode);
    res.on('data', function (body) {
        console.log('Result : \n'+body); //imprimindo o resultado
    })

});


//Criando o JSON do produto a ser inserido
var inserirProduto = {
    titulo : '',
    descricao : 'Livro inserido via JSON',
    preco : 99.9
};

//encaminhando a solicitação JSON
request.end(JSON.stringify(inserirProduto));