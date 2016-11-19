/**
 * Created by luizmiccieli on 14/11/16.
 */

module.exports = function (app) { //falando que esse modulo export essa funçao passando o app
    app.get('/pagamentos', function (req, res) {
        console.log('recebida a requisicao de teste ');
        res.send('ok');
    });


    app.put('/pagamentos/pagamento/id=:id/:status', function (req, res, next) {
       var pagamento = {};
        pagamento.id = req.params.id;
        pagamento.status = req.params.status;


        console.log('Pagamento que será alterado: '+pagamento);
        var connection = app.dao.connectionFactory();
        var pagamentoDAO = new app.dao.pagamentoDAO(connection);

        pagamentoDAO.atualiza(pagamento, function (erro) {
            if(erro){
                res.status(500).json({ 'pagamento': pgamento, 'Error': erro} )
            }
        })

        res.send(pagamento);

    });
    /*curl http://localhost:3000/pagamentos/pagamento -X POST -v -H "Content-type: application/json" -d '
    "forma_de_pagamento":"payfast",
        "valor":10.98,
        "moeda":"BRL",
        "descricao":"criando um pagamento"
}'; echo
*/
    app.post('/pagamentos/pagamento', function (req,res, next) {

        req.assert("forma_de_pagamento","Forma de pagamento é obrigatorio").notEmpty();
        req.assert("preco", "não pode ser vazio e deve ser decimal").notEmpty().isFloat();
        req.assert("moeda", "Não pode ser vazio e deve ter no maximo 3 caracteres").notEmpty().len(3,3);

        var errosValidacao = req.validationErrors();
        if(errosValidacao){
            console.log("Erros de validacao:");
            console.log(errosValidacao);

            res.status(400).json(errosValidacao);
            return next();
        }


        var pagamento = req.body;
        console.log('Recebuda a requisição de post');
        console.log('Corpo Pagamengo:');

        pagamento.status = 'CRIADO';
        pagamento.data = new Date();

        console.log(pagamento);

        //salvando pagamento
        var connection = app.dao.connectionFactory();
        var pagamentoDAO = new app.dao.pagamentoDAO(connection);

        pagamentoDAO.salva(pagamento,  function (err, result){
            if(err){
                res.status(500).json({error: 'Não foi possivel salvar no banco', eror_desc: err });
                return next(err);
            }
            console.log('Pagamento criado');
            res.location('/pagamentos/pagamento/id='+result.insertId); //insertId é um parametro do connector do mysql
            res.status(201).json(pagamento); //status 201 indica que algo foi criado
        });

    });
};


/*
Status code
familias
100 -> conexao continuada
200 -> ok
300 -> redirecionamentos
400 -> erros de entrada de usuário
500 -> erros interno do servidor
 */