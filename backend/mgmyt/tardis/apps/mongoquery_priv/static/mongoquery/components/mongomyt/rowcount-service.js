function RowcountService($resource) {  
  /**
   * @name GameService
   *
   * @description
   * A service providing game data.
   */

  var that = this;

  /**
   * A resource for retrieving game data.
   */
  that.RowcountResource = $resource(_urlPrefixes.API + "collections_list/"+{params:{code:code}+"/");

  /**
   * A convenience method for retrieving Game objects.
   * Retrieval is done via a GET request to the ../games/ endpoint.
   * @param {object} params - the query string object used for a GET request to ../games/ endpoint
   * @returns {object} $promise - a promise containing game-related data
   */
  that.getRowcount = function(params) {
    return that.RowcountResource.query(params).$promise;
  };
}

angular.module("Rowcount")  
  .service("RowcountService", ["$resource", RowcountService]);

