/**
 * Created by luizmiccieli on 02/11/16.
 */
var http = require('http');
var server = http.createServer(function (req,res) {
    if(req.url == '/produtos'){
        res.end('<html><body><h1>listando os produtos</h1></body></html>');
    }else{
        res.end('<html><body><h1>home</h1></body></html>');
    }
});
server.listen(3000);

console.log('Servidor rodando');