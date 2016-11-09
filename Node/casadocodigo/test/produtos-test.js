/**
 * Created by ter00409 on 09/11/2016.
 */
/**
 * O MOCHA precisa que os testes estejam dentro da pasta test na raiz do projeto
 * as funções de test do mocha, devem comecar como descibe
 */

/**
 * Case de test de produtos
 */
var http = require('http');
var assert = require('assert'); //modulo de verificacao de teste


describe('ProdutosController', function () {

    /**
     * Caso de teste reponsavel em verificar se o servidor está aceitando e retornando os produtos via JSON
     */
    it('#listagem json', function (done) { //necessario passar para que o MOCHA saiba que a funcao assincrona tenha acabado de fato
       //gerando json responsavel pela listagem de produtos no servidor
        var config = {
            hostname : 'localhost',
            port : 3000,
            path : '/produtos',
            headers : {
                'Accept' : 'application/json'
            }
        };

        //fazendo o get do JSON
        http.get(config,function (res) {


            //verificando se o status code é igual a 200 (sucesso)
            assert.equal(res.statusCode,200);
            assert.equal(res.headers['content-type'],'application/json; charset=utf-8');


            done();
        });
        
    });

});
