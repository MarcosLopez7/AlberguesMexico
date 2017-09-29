/**
 * Created by marcoslopez7 on 9/23/17.
 */
(function () {
    angular.module('fronterApp', [])
        .config(function ($interpolateProvider, $httpProvider) {
            $interpolateProvider.startSymbol('{$');
            $interpolateProvider.endSymbol('$}');

            $httpProvider.defaults.xsrfCookieName = 'csrftoken';
            $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
        });
}());