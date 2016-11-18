/**
 * Created by luizmiccieli on 02/11/16.
 */
//chamando o arquivo de configuração
var app = require('./config/configExpress')();

var http = require('http').Server(app); //chamando novamente o http para configurar o socket.io
var io = require('socket.io')(http);

app.set('io',io); //setando a variael do Socket IO no express

//chamando rotas, passando a configuração do express
require('./app/routes/Produtos')(app);


var server = http.listen(3000, function () {
    var port = server.address().port;
    console.log('App está rodando na porta: %s', port);
});


