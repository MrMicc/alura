/**
 * Created by luizmiccieli on 14/11/16.
 */

module.exports = function (app) { //falando que esse modulo export essa funçao passando o app
    app.get('/pagamentos', function (req, res) {
        console.log('recebida a requisicao de teste ');
        res.send('ok');
    });

    /*curl http://localhost:3000/pagamentos/pagamento -X POST -v -H "Content-type: application/json" -d '
    "forma_de_pagamento":"payfast",
        "valor":10.98,
        "moeda":"BRL",
        "descricao":"criando um pagamento"
}'; echo
*/
    app.post('/pagamentos/pagamento', function (req,res) {
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
            console.log(err);
            console.log('Pagamento criado');
            res.json(pagamento);
        });

    });
};
