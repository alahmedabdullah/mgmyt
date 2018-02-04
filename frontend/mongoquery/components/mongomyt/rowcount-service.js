function RowcountService($resource) {  

  var that = this;

  that.RowcountResource = $resource(_urlPrefixes.API + "collections_list/"+{params:{code:code}+"/");

  that.getRowcount = function(params) {
    return that.RowcountResource.query(params).$promise;
  };
}

angular.module("Rowcount")  
  .service("RowcountService", ["$resource", RowcountService]);

