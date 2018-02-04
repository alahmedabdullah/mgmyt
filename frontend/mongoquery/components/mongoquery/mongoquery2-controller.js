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

  that.downloadResult = function() {
    if (that.mongo_result){
        var mongo_result_string = JSON.stringify(that.mongo_result);
        var blob = new Blob([mongo_result_string], {type: "text/plain"});
        var fileName = "mongo_query_result.json"
        //var objectUrl = URL.createObjectURL(blob);
        window.saveAs(blob, fileName);
    };
          
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
