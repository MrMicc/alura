/**
 * Created by ter00409 on 03/11/2016.
 */

//exportando rota que lista produtos
module.exports = function (app) {
    app.get('/produtos',function (req,res) {
        console.log('Listando os produtos');
        /*var mysql = require('mysql');
        var connection = mysql.createConnection({
            host : 'localhost',
            user: 'root',
            password: '',
            database: 'casadocodigo'
        });*/
        var sqlite = require('sqlite3');
        var connection = new sqlite.Database('casadocodigo.db'); //mysql -> createConnection({host: '', user:'', password:'', database:''})

        connection.all('SELECT * FROM livros', function (err, result) { //mysql -> query
            console.log(err);
            res.send(result); // encaminhando para a view
        });

        connection.close(); //mysql -> end


        //res.render('produtos/lista');
    })
};