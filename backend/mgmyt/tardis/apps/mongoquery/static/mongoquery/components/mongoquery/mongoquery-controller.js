function MongoqueryController(MongoqueryService, $routeParams) {  
  var that = this;

  that.mongo_result = [];
  that.loading = false;
  that.formsubmitted = false;
  that.waitmsg = "Waiting for response, please wait...";
  that.collection_name= $routeParams.collection_name;
  
  that.setFormSubmitted = function(){
    that.formsubmitted =  true;
  };

  that.submitQuery = function(query_param2) { 
    return MongoqueryService.submitQuery(that.collection_name,query_param2).then(function(query_param2) {
      that.mongo_result = query_param2;
    }).finally(function () {
       that.loading = true;
       that.formsubmitted =  false;
    });
  };
}

angular.module("Mongoquery")  
  .controller("MongoqueryController", [
    "MongoqueryService", 
    "$routeParams",
    MongoqueryController
  ]);
