/**
 * Created by ter00409 on 03/11/2016.
 */

//exportando rota que lista produtos
module.exports = function (app) {
    app.get('/produtos',function (req,res) {
        console.log('Listando os produtos');
        res.render('produtos/lista');
    })
};