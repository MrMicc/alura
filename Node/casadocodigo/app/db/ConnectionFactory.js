/**
 * Created by luizmiccieli on 05/11/16.
 */
var mysql = require('mysql');

var connectMYSQL  = function() {
    console.log('Retornando conexão da Fábrica');
   return mysql.createConnection({
        host : 'localhost',
        user: 'root',
        password: 'root',
        database: 'casadocodigo'
    });
    if(!process.env.NODE_ENV){
       return mysql.createConnection({
            host : 'localhost',
            user: 'root',
            password: '',
            database: 'casadocodigo'
        });
    }
    if(process.env.NODE_ENV == 'test'){
        return mysql.createConnection({
            host : 'localhost',
            user: 'root',
            password: '',
            database: 'casadocodigo_test'
        });
    }

};


module.exports = function () {
    console.log('Preparando a factory');
    return connectMYSQL;
};