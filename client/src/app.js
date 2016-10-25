var app = angular.module('app', ['ngMaterial']);

app.controller('emailsController', function ($scope, $http) {
    $scope.emails = null;
    var responsePromise = $http.get("/emails/");

    responsePromise.success(function(data, status, headers, config) {
        console.log(data);
        $scope.emails = data;
    });
    responsePromise.error(function(data, status, headers, config) {
        $scope.emails = [
        ];
    });
});

app.controller('NavCtrl', function ($scope, $timeout, $mdSidenav, $log) {
    $scope.toggle = function () {
       $mdSidenav('nav').toggle();
    }
});