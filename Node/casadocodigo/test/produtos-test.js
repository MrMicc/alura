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

var express = require('../config/configExpress')();
var request = require('supertest')(express);

//var assert = require('assert'); //modulo de verificacao de teste


describe('#ProdutosController', function () {

    /**
     * Caso de teste reponsavel em verificar se o servidor está aceitando e retornando os produtos via JSON
     */
    beforeEach(function (done) {
        //node-database-cleanner PESQUISAR
       var conn = express.db.ConnectionFactory();
        conn.query('DELETE FROM livros', function (err, result) {
           if(!err){
               done();
           }
        });
    });

    it('#listagem json', function (done) { //necessario passar para que o MOCHA saiba que a funcao assincrona tenha acabado de fato
        request.get('/produtos')
            .set('Accept', 'application/json') // informando que no header da requisiçao tem que ser do tipo JSON
            .expect(200)
            .expect('Content-Type', /json/)   //falando que a resposta esperada no contet-type tem que ter a palavara json
            .end(done);//informando que espera um statusCode 200 e que pode finalizar o teste
    });

    it('#listagem html', function (done) { //necessario passar para que o MOCHA saiba que a funcao assincrona tenha acabado de fato
        request.get('/produtos')
            .expect('Content-Type', /html/)   //falando que a resposta esperada no contet-type tem que ter a palavara HTML
            .expect(200)
            .end(done);//informando que espera um statusCode 200 e que pode finalizar o teste
    });


    it('#cadastro de produtos com titulo vazio', function (done) {
        request.post('/produtos')
            .send({titulo : '', descricao: 'Novo livro', preco: '44'})
            .expect(400,done);
    });

    it('#cadastro de produtos com preco vazio', function (done) {
        request.post('/produtos')
            .send({titulo : 'Titulo', descricao: 'Novo livro', preco: ''})
            .expect(400,done);
    });

    it('#cadastro de produtos com preco string', function (done) {
        request.post('/produtos')
            .send({titulo : 'Titulo', descricao: 'Novo livro', preco: 'asd'})
            .expect(400,done);
    });

    it('#cadastro de produtos sucesso', function (done) {
        request.post('/produtos')
            .send({titulo : 'Titulo TEste', descricao: 'Novo livro Teste', preco: '40'})
            .expect(302,done);  //status 302 pois é feito um redirect no sucesso
    });
    it('#cadastro de produtos sucesso sem descricao', function (done) {
        request.post('/produtos')
            .send({titulo : 'Titulo Teste Sem Descr', descricao: '', preco: '40'})
            .expect(302,done); //status 302 pois é feito um redirect no sucesso
    });

});
