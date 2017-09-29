/**
 * Created by marcoslopez7 on 9/25/17.
 */
(function () {
  'use strict';

  angular.module('fronterApp')
      .controller('refugeController', function ($scope, refugeService, $window) {

          $scope.refuge = {
              name: '',
              refuge: '',
              location: '',
              city: '',
              state: '',
              user: 0,
              post: {
                  description: '',
                  enable_beds: '',
                  needs: []
              }
          };

          $scope.need = {
              product: '',
              quantity: ''
          };

          $scope.user_id = '';

          $scope.init = function (id) {
              $scope.refuge.user = id;
              $scope.needing = false;
          };

          $scope.createNeed = function () {
              $scope.refuge.post.needs.push($scope.need);
              $scope.needing = false;
              $scope.need = {
                  product: '',
                  quantity: 0
              };
          };

          $scope.deleteNeed = function (need) {
              var index;

              for (var i = 0; i < $scope.refuge.post.needs.length; i++){
                  if (need === $scope.refuge.post.needs[i]) {
                      index = i;
                      break;
                  }
              }

              $scope.refuge.post.needs.splice(index, 1);
          };

          $scope.createRefuge = function () {

              $scope.refuge.post.enable_beds = parseInt($scope.refuge.post.enable_beds);

              for (var i = 0; i < $scope.refuge.post.needs.length; i++) {
                  $scope.refuge.post.needs[i].quantity = parseInt($scope.refuge.post.needs[i].quantity);
              }

              refugeService.postRefuge($scope.refuge, function (response) {
                  $window.location.href = '/';
              }, function (response) {
                  alert("Algo inesperado sucedio");
                  console.log(response);
              });
          };

      });
}());