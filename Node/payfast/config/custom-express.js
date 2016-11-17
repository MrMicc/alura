/**
 * Created by luizmiccieli on 14/11/16.
 */

var express = require('express'); //carregando o arquivo do express
var consign = require('consign');
var bodyParser = require('body-parser');


module.exports = function () {
    var app = express(); //invocando o express

    app.use(bodyParser.urlencoded({extended: true}));
    app.use(bodyParser.json());

    consign() //inserindo a pasta controllers no express
        .include('controllers')
        .then('dao')
        .into(app);



    return app;
};