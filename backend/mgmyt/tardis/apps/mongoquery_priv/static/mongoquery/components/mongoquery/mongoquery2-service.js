function Mongoquery2Service($resource) {  
  var that = this;

  that.submitQuery = function(param1,param2) {
    if (param2) {
        that.Mongoquery2Resource = $resource(_urlPrefixes.API + "getquery" + "/" + param1 + "/ " );
        return that.Mongoquery2Resource.save({ "query_text" : param2.query_text } ).$promise;

    }
  };

}

angular.module("Mongoquery2")  
  .service("Mongoquery2Service", ["$resource", Mongoquery2Service]);

