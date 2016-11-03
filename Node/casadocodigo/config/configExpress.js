/**
 * Created by ter00409 on 03/11/2016.
 */
var express = require('express');
var app = express();

//Exportando o modulo responsavel em configurar o express
module.exports = function () {
    app.set('view engine', 'ejs');
    app.set('views','./app/views');

    return app;
};