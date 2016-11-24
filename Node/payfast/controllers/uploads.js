/**
 * Created by luizmiccieli on 22/11/16.
 */
var fs = require('fs');

module.exports = function (app){
  app.post('/uploads/imagem', function (req, res, next) {
      console.log('Recebendo a imagem');

      var filename = req.headers.filename;
      console.log('Nome do arquivo: '+filename);
      req.pipe(fs.createWriteStream('files/'+filename))
          .on('finish', function () { //é necessario o on, para setarmos um listener de finish e passar um callback
              console.log('Arquivo salvo: '+filename);
              res.status(201).json({'status':'OK - Enviado'})
          });



  });
};