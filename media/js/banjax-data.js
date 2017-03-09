Banjax.data = (function () {
 
	function getCookie(name) {
    	var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    	return r ? r[1] : undefined;
	 }

  	var postData = function(url, data, successCallback) {
      	xsrf = getCookie("_xsrf");
      	$.ajax({url: url, 
      			data: {"xmlData": data, "_xsrf": xsrf}, 
      			dataType: "text", 
      			type: "POST",
         		success: successCallback,
         		error: function(){console.log('bugger did not work')} });
	};
 
  	return {
    	post: postData,
  	};
 
})();




