/**
 * Created by luizmiccieli on 14/11/16.
 */
var app = require('./config/custom-express')();//carregando e invocando o codigo ()

var server = app.listen(3000, function () { //setando a porta 3000 como a default da aplicacao
    console.log('Servidor rodandno na porta: %s', server.address().port);
});


