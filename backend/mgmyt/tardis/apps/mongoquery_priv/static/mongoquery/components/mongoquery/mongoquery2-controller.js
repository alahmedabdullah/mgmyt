function Mongoquery2Controller(Mongoquery2Service, $routeParams) {  
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
    return Mongoquery2Service.submitQuery(that.collection_name,query_param2).then(function(query_param2) {
      that.mongo_result = query_param2;
    }).finally(function () {
       that.loading = true;
       that.formsubmitted =  false;
    });
  };
}

angular.module("Mongoquery2")  
  .controller("Mongoquery2Controller", [
    "Mongoquery2Service", 
    "$routeParams",
    Mongoquery2Controller
  ]);
