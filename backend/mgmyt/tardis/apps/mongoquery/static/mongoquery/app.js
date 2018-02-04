/* Libs */
require("angular/angular");  
require("angular-route/angular-route");  
require("angular-resource/angular-resource");

/* Globals */
_ = require("lodash");  
_urlPrefixes = {  
  API: "mongoquery/api/v1/",
  TEMPLATES: "static/mongoquery/"
};

/* Components */
require("./components/home/home");
require("./components/mongomyt/mongomyt");
require("./components/mongoquery/mongoquery");

/* App Dependencies */
var app = angular.module("myApp", [  
  "Home", 
  "Mongomyt",
  "Mongoquery",
  "ngResource",
  "ngRoute",
]);

/* Config Vars */
var routesConfig = require("./routes");

/* App Config */
app.config(routesConfig);
