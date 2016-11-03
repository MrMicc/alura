/**
 * Created by ter00409 on 03/11/2016.
 */
var express = require('express');
var app = express();

module.exports = function () {
    app.set('view engine', 'ejs');

    return app;
}