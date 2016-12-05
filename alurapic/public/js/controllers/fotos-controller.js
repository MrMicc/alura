/**
 * Created by luizmiccieli on 30/11/16.
 */
/*
requisição ajax $http
bindings -> $scope
 */
angular.module('alurapic').controller('FotosController', function ($scope, $http) {

    $scope.fotos =[];

    $scope.filtro = '';

    /*utilizando atalho */
    $http.get('v1/fotos').success(function (fotos) {
        $scope.fotos = fotos;
    }).error(function (error) {
        console.log(error);
    });

    /*Promise
    //quando for realizado o promise, então colocamos os dados no scope
    promise.then(function (retorno) {
       $scope.fotos = retorno.data;
    }).catch(function (error) {
        console.log('Error ----> '.error);
    }); */
});
