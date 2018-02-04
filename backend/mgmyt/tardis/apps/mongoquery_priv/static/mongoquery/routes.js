function routesConfig($routeProvider,$httpProvider) {  
  $routeProvider
    .when("/mongoquery", {
      templateUrl: _urlPrefixes.TEMPLATES + "components/mongomyt/mongomyt.html",
    })
    .when("/mongoquery/:collection_name", {
      templateUrl: _urlPrefixes.TEMPLATES + "components/mongoquery/mongoquery.html",
    })
    .otherwise("/mongoquery");
   
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}


routesConfig.$inject = ["$routeProvider","$httpProvider"];

module.exports = routesConfig;
