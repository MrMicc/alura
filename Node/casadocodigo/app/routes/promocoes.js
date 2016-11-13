/**
 * Created by luizmiccieli on 12/11/16.
 */

module.exports = function (app) {
    /**
     * Renderizando o formulario de promocoes relampago
     */
    app.get('/promocoes/form', function (req,res,next) {
        var connection = app.db.ConnectionFactory();
        var produtosDAO = app.db.ProdutosDAO(connection);

        produtosDAO.lista(function (err, produtos) {
            if(err != null){
                return next(err);
            }else{
                res.render('./promocoes/form', {errosValidacao: {}, lista : produtos});
            }
        });
        connection.end();
    });

    /**
     * Realizando o post do formulario de promocoes relampago
     */
    app.post('/promocoes', function (req, res) {
        var promocao = req.body; //pegando a tag em formato JSON

        var connection = app.db.ConnectionFactory();
        var produtosDAO = app.db.ProdutosDAO(connection);

        //fazendo validação
        req.assert('mensagem', 'Mensagem da promocao é obrigatoria').notEmpty();

        var erros = req.validationErrors();
        if(erros){

            produtosDAO.lista(function (err, produtos) {
                res.status(400).render('./promocoes/form',{errosValidacao:erros, lista: produtos});
            });
            return;
        }
        //fim da validacao
        produtosDAO.getProduto(promocao.livro.id, function (err, result) {
            if(err != null){
                console.log(err);
            }
            var livro = result[0]; //pegando o unico livro retornado
            app.get('io').emit('novaPromocao',livro); //enviando a promoção do livro escolhido via Socket.io
        });

        res.redirect('./promocoes/form');

    });


};

function getProdutos(app, req, res, next){

}

