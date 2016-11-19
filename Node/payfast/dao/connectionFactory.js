/**
 * Created by luizmiccieli on 17/11/16.
 */

var mysql = require ('mysql');

function createDBConnection() {
    return mysql.createConnection({
        host : 'localhost',
        user: 'root',
        password: '',
        database: 'payfast'
    });

}

module.exports = function () {
    return createDBConnection;
};