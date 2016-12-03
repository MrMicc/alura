/**
 * Created by luizmiccieli on 03/12/16.
 */

angular.module('minhasDiretivas',[]).directive('meuPainel', function () {
   var ddo = {}; //directive document object

   ddo.restrict = 'AE';

   ddo.scope = {
       titulo : '@titulo'
   };

   ddo.transclude = true;

   ddo.templateUrl = './js/directives/html/meuPainel.html';

   return ddo;

});
