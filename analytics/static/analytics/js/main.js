$(document).ready(function () {
	 function initialize() {
	    var mapOptions = {
	      center: { lat: 28.6139, lng: 77.2090},
	      zoom: 12
	    };
	    var map = new google.maps.Map(document.getElementById('map'),
	        mapOptions);
	  }
	  google.maps.event.addDomListener(window, 'load', initialize);
});