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
 
  	return {
    	post: postData,
  	};
 
})();




