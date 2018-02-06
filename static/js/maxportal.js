var app = angular.module('myapp', []);
app.controller('myctl', function($scope, $http){
			//$scope.startdate = "testtttt";
			//$scope.enddate = "tttttttttest";
			$scope.query = function(){
				//$scope.period = "from "+$scope.startdate+" to "+$scope.enddate;
				$http({
					method: 'GET',
					url: 'http://localhost:8090/timeentry/api/labtrans/',
				}).then(
					function successCallback(response){
						$scope.count = response.data.count;
						$scope.records = response.data.results;
					},
					function errorCallback(response){
						$scope.error = 'There is error happened!';
					},
				);
			};
			//$scope.query();
		});