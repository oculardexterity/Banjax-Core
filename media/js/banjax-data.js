Banjax.data = (function () {
 
	function getCookie(name) {
    	var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    	return r ? r[1] : undefined;
	 }

  	var postData = function(url, data, successCallback, errorCallback) {
      	xsrf = getCookie("_xsrf");
      	$.ajax({url: url, 
      			data: {"xmlData": data, "_xsrf": xsrf}, 
      			dataType: "text", 
      			type: "POST",
         		success: successCallback,
         		error: errorCallback});
	};

    function current_item() {
        var itemloaded = window.location.href.split('/');
        itemloaded = itemloaded[itemloaded.length -1]
        //console.log(itemloaded);
        return itemloaded
    }
 
  	return {
    	post: postData,
        current_item: current_item
  	};
 
})();




