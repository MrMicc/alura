/**
 * Created by luizmiccieli on 14/11/16.
 */

var express = require('express'); //carregando o arquivo do express
var consign = require('consign'); //modulo responsavel em carregar arquivos
var bodyParser = require('body-parser'); //modulo responsavel em parsear json e html
var expressValidator = require('express-validator'); //modulo responsavel em validcao
var logger = require('../services/logger.js');



module.exports = function () {
    var app = express(); //invocando o express

    app.use(bodyParser.urlencoded({extended: true}));
    app.use(bodyParser.json());
    app.use(expressValidator());

    logger.debug("Overriding 'Express' logger");
    app.use(require('morgan')({ "stream": logger.stream }));

    consign() //inserindo a pasta controllers no express
        .include('controllers')
        .then('dao')
        .then('services')
        .into(app);



    return app;
};