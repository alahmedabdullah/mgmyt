function MongomytService($resource) {  
  /**
   * @name GameService
   *
   * @description
   * A service providing game data.
   */

  var that = this;

  /**
   * A resource for retrieving game data.
   *
   * that.MongomytResource = $resource(_urlPrefixes.API + "collections_list/" + {params:{code:code}} + "/");
   * that.MongomytResource = $resource(_urlPrefixes.API + "collections_list/:collection_name/");
   */


  /**
   * A convenience method for retrieving Game objects.
   * Retrieval is done via a GET request to the ../games/ endpoint.
   * @param {object} params - the query string object used for a GET request to ../games/ endpoint
   * @returns {object} $promise - a promise containing game-related data
   */

  that.getCollections = function(param1,param2) {
  /**
   * that.MongomytResource = $resource(_urlPrefixes.API + param1 +"/" + param2+"/");
   */
    if (param2) {
        //that.MongomytResource = $resource(_urlPrefixes.API + param2 + "/" );
        that.MongomytResource = $resource(_urlPrefixes.API + param1 +"/" + param2+"/");
        //parma2="";
        return that.MongomytResource.get(param2).$promise;
    } else {
        that.MongomytResource = $resource(_urlPrefixes.API + param1 +"/" );
        return that.MongomytResource.get(param1).$promise;

    }
  };

}

angular.module("Mongomyt")  
  .service("MongomytService", ["$resource", MongomytService]);

