function routesConfig($routeProvider,$httpProvider) {  
  $routeProvider
    .when("/", {
      templateUrl: _urlPrefixes.TEMPLATES + "components/mongomyt/mongomyt.html",
      label: "Home"
    })
    .when("/mongomyt", {
      templateUrl: _urlPrefixes.TEMPLATES + "components/mongomyt/mongomyt.html",
      label: "Mongomyt"
    })
    .when("/mongoquery/:collection_name", {
      templateUrl: _urlPrefixes.TEMPLATES + "components/mongoquery/mongoquery.html",
      label: "Mongoquery"
    })
    .otherwise({
      templateUrl: _urlPrefixes.TEMPLATES + "404.html"
    });
   
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}


routesConfig.$inject = ["$routeProvider","$httpProvider"];

module.exports = routesConfig;
