/**
 * Created by luizmiccieli on 02/11/16.
 */

var app = require('./config/configExpress')(); //chamando o arquivo de configuração


app.get('/produtos',function (req,res) {
    console.log('Listando os produtos');
    res.render('produtos/lista')
})

app.listen(3000, function () {
    console.log('Servidor rodando!!');
});


