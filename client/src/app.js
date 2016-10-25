var app = angular.module('app', ['ngMaterial']);

// No reason to split this to different files as we do when we have more lines of code
app.controller('emailsController', function ($scope, $http) {
    $scope.emails = null;
    var responsePromise = $http.get("/emails/");

    responsePromise.success(function(data, status, headers, config) {
        $scope.emails = data;
    });
    responsePromise.error(function(data, status, headers, config) {
        $scope.emails = [];
        $scope.error = "Error retreiving data."
    });
});

app.controller('NavCtrl', function ($scope, $timeout, $mdSidenav, $log) {
    $scope.toggle = function () {
       $mdSidenav('nav').toggle();
    }
});