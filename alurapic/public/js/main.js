/**
 * Created by luizmiccieli on 30/11/16.
 */
angular.module('alurapic',['minhasDiretivas', 'ngAnimate', 'ngRoute']).config(function ($routeProvider, $locationProvider) {
    $locationProvider.html5Mode(true);

    $routeProvider.when('/', {
        templateUrl : './partials/principal.html',
        controller : 'FotosController'
    });

    $routeProvider.when('/fotos/new', {
        templateUrl : './partials/newFoto.html'
    });


});
