function MongoqueryService($resource) {  
  var that = this;

  that.submitQuery = function(param1,param2) {
    if (param2) {
        that.MongoqueryResource = $resource(_urlPrefixes.API + "getquery" + "/" + param1 + "/ " );
        return that.MongoqueryResource.save({ "query_text" : param2.query_text } ).$promise;

    }
  };

}

angular.module("Mongoquery")  
  .service("MongoqueryService", ["$resource", MongoqueryService]);

