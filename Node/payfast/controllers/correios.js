/**
 * Created by ter00409 on 21/11/2016.
 */

module.exports = function (app) {
  app.post('/correios/calculo-prazo', function (req, res, next) {
      var bodyDadosEntrega = req.body;


      var clientCorreios = new app.services.clientSOAPCorreios();
      clientCorreios.calculaPrazo(bodyDadosEntrega, function (error, result) {
          if(error){
              console.log('ERRO ao calcular Prazo de entrega: '+error);
              res.status(500).json(error);
              return next(error);
          }else{
              resultJson = JSON.stringify(result);
              console.log('Retorno do calculo do prazo de entrega: '+resultJson);
              res.status(200).json(resultJson);
          }
      })

  });
};