function MongomytService($resource) {  
  var that = this;

  /**
   * that.MongomytResource = $resource(_urlPrefixes.API + "collections_list/" + {params:{code:code}} + "/");
   * that.MongomytResource = $resource(_urlPrefixes.API + "collections_list/:collection_name/");
   */

  that.getCollections = function(param1,param2) {
  /**
   * that.MongomytResource = $resource(_urlPrefixes.API + param1 +"/" + param2+"/");
   */
    if (param2) {
        that.MongomytResource = $resource(_urlPrefixes.API + param1 +"/" + param2+"/");
        return that.MongomytResource.get(param2).$promise;
    } else {
        that.MongomytResource = $resource(_urlPrefixes.API + param1 +"/" );
        return that.MongomytResource.get(param1).$promise;

    }
  };

}

angular.module("Mongomyt")  
  .service("MongomytService", ["$resource", MongomytService]);

