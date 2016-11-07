/**
 * Created by ter00409 on 03/11/2016.
 */
var express = require('express');
var load = require('express-load');
var bodyParser = require('body-parser');

//Exportando o modulo responsavel em configurar o express
module.exports = function (){
    var app = express();

    app.set('view engine', 'ejs');
    app.set('views','./app/views');

    app.use(bodyParser.urlencoded({extended:true}));
    app.use(bodyParser.json());

    load('routes',{cwd : 'app'})
        .then('db')
        .into(app);

    return app;
};