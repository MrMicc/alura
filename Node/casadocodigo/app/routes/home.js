/**
 * Created by luizmiccieli on 12/11/16.
 */

module.exports = function (app) {
    app.get('/',function (req, res, next) {
        var connection = app.db.ConnectionFactory();
        var produtosDAO = app.db.ProdutosDAO(connection);

        produtosDAO.lista(function (err, produtos) {
           if (err !=null){
               return next(err);
           }else {
               console.log('Renderizando index');
               res.render('./home/index', {livros: produtos});
           }
        });
        connection.end();
    })
}
