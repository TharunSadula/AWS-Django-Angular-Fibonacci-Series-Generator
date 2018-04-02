(function() {
    'use strict';

    angular.module('core', [])
        .controller('coreController',
            [ '$scope', '$http', coreController ]);

    function coreController($scope, $http) {
        $scope.getfib = function(form){
            if(form.$invalid){
          return form
            }
            $http.get('/fib/'+$scope.fibnumber).then(
            function(response){
              $scope.result = response.data[0].fib;
            }
            );
        }

        $scope.erase=function(){
        $scope.result=null;
        }

    }

}());