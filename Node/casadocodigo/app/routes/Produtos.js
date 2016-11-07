/**
 * Created by ter00409 on 03/11/2016.
 *
 * controller responsável pelas rotas dos produtos
 */


//exportando rota que lista produtos
module.exports = function (app) {
    app.get('/produtos',function (req,res) {
        console.log('Listando os produtos');

        console.log('Carregando a conection da fábrica');
        var connection = app.db.ConnectionFactory();
        var produtosBanco = new app.db.ProdutosDAO(connection);

        produtosBanco.lista(function(err, result){
            if(err != null){
                console.log(err);
            }else{
                console.log('Retornou livros ' +result.length);
                //retornando dois tipo de retornos possiveis JSON e HTML
                res.format({
                    html : function(){
                       res.render('./produtos/lista',{lista:result});
                   },
                    json : function () {
                        res.json(result);
                    }
                })
            }
        });
        connection.end();
    });

    app.get('/produtos/form',function (req,res) {
        res.render('./produtos/form');
    });
    
    
    app.post('/produtos', function (req,res) {
        var produto = req.body; //pegando as tags do form e transformando em JSON

        var connection = app.db.ConnectionFactory();
        var produtosBanco = new app.db.ProdutosDAO(connection);
        produtosBanco.salvaProduto(produto,function (err, result) {
            if(err!=null){
                console.log(err);
            }else{
                res.redirect('/produtos'); //redirecionando para o pagina que lista
            }
        })

    });


     app.get('/produtos/delete', function (req, res) {
         res.render('./produtos/delete');
     });

    app.post('/produtos/delete',function (req, res) {
        var produtoDelete = req.body;

        var connection = app.db.ConnectionFactory();
        var produtosBanco = new app.db.ProdutosDAO(connection);
        produtosBanco.delete(produtoDelete,function (err,result) {
            if(err!=null){
                connection.log(err);
            }else{
                res.redirect('/produtos');
            }
        })

    })
};