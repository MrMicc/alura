/**
 * Created by luizmiccieli on 14/11/16.
 */

module.exports = function (app) { //falando que esse modulo export essa funçao passando o app
    app.get('/pagamentos', function (req, res) {
        console.log('recebida a requisicao de teste ');
        res.send('ok');
    });

    app.delete('/pagamentos/pagamento/id=:id', function (req, res) {
        atualizaStatus(req,res, { desc : 'CANCELADO', code: '204'} );
    });

    app.put('/pagamentos/pagamento/id=:id/', function (req, res) {
       atualizaStatus(req,res, { desc: 'CONFIRMADO', code : '200'});

    });

    /**
     * Metodo responsavel em realizar a autualizacao do status de forma generica passando os seguintes parametros
     * @param req - requisicao
     * @param res - response
     * @param status - status code de retorno no response
     */
    function atualizaStatus(req, res, status){
        var pagamento = {};
        pagamento.id = req.params.id;
        pagamento.status = status.desc;

        console.log('Pagamento que será alterado: '+pagamento.id+ 'para status: '+pagamento.status);
        var connection = app.dao.connectionFactory();
        var pagamentoDAO = new app.dao.pagamentoDAO(connection);

        pagamentoDAO.atualiza(pagamento, function (erro) {
            if(erro){
                res.status(500).json({ 'pagamento': pgamento, 'Error': erro} )
            }
        });

        console.log(req.socket.server);
        res.status(status.code).send(pagamento);

    }
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

            pagamento.id = result.insertId;
            console.log('Pagamento criado');
            res.location('/pagamentos/pagamento/id='+pagamento.id); //insertId é um parametro do connector do mysql

            var response = {
                dados_do_pagamento: pagamento,
                links: [
                    {
                        href: '/pagamentos/pagamento/id='+pagamento.id,
                        rel: 'CONFIRMAR',
                        method: 'PUT'
                    },
                    {
                        href: '/pagamentos/pagamento/id='+pagamento.id,
                        rel: 'CANCELAR',
                        method: 'DELETE'
                    }
                ]
            };

            res.status(201).json(response); //status 201 indica que algo foi criado
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