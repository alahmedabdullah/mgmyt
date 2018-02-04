function MongomytListController(MongomytService) {  
  var that = this;

  /* Stored game objects. */
  that.the_collections = [];
  that.loading = true;
  that.waittext = "??";

  /**
   * Initialize the game list controller.
   */
  that.init = function(collection_param1, collection_param2) { 
    return MongomytService.getCollections(collection_param1,collection_param2).then(function(collection_param1) {
      that.the_collections = collection_param1;
    }, function(collection_param2){
      that.the_collections = collection_param2;
    }).finally(function () {
       that.loading = false;
    });
  };
}

angular.module("Mongomyt")  
  .controller("MongomytListController", [
    "MongomytService",
    MongomytListController
  ]);
