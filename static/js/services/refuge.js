/**
 * Created by marcoslopez7 on 9/25/17.
 */
(function () {
  'use strict';

  var ip = 'http://localhost:8000/';

  angular.module('fronterApp')
      .service('refugeService', function ($http) {
          this.postRefuge = function (params, callback, error) {
              $http.post(ip + 'create-refuge/', params).then(callback).catch(error);
          }
      })

}());