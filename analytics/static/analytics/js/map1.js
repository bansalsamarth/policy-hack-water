$(document).ready(function(){
 		var STATIC_URL = "http://localhost:8001/static/analytics/images/"
        var map;
        var snappedCoordinates1 = [];
        var snappedCoordinates2 = [];
        var snappedCoordinates3 = [];
        var snappedCoordinates4 = [];
        var placeIdArray =[];
        var polylines = [];
        var drawingManager;
        var tankMarker;
 
        var getLocationDataForTanker = function() {
          var mapOptions = {
              zoom: 11,
              center: {lat: 28.6284909, lng: 77.2222353}
          };
          map = new google.maps.Map(document.getElementById('map'), mapOptions);
          var myLatlng = new google.maps.LatLng(28.634592,77.217321);
 
           var myLatlng1 = new google.maps.LatLng(28.709861,77.176552);
           var myLatlng2 = new google.maps.LatLng(28.56613,77.253456);
          marker1 = new google.maps.Marker({
              position: myLatlng1,
              map: map,
              title:"Truck 1"
          });
           marker2 = new google.maps.Marker({
              position: myLatlng2,
              map: map,
              title:"Truck 2"
           });
          //   marker3 = new google.maps.Marker({
          //     position: myLatlng,
          //     map: map,
          //     title:"Truck 3",
          //      icon: STATIC_URL + "fuel_tanker.png"
          // });
          //    marker4 = new google.maps.Marker({
          //     position: myLatlng,
          //     map: map,
          //     title:"Truck 4",
          //      icon: STATIC_URL + "fuel_tanker.png"
          // });
              var qs = "";
              getSnappedCoordinates(qs);
          // $.get("dist/js/testRoute.json", function(data){
          //     console.log(data);
 
          //     console.log(qs);
          // });
 
        }
 
 
        var getCoordinatesForRoadSnapping = function(data) {
 
          var maxLength = 100;
          if (maxLength > data.data.length) {
              maxLength = data.data.length;
          }
          var queryString = "";
          for(var i=0;i<maxLength;i++) {
              queryString += data.data[i].latitude + ","+data.data[i].longitude;
              if(i!=maxLength-1){
                  queryString += "|";
              }
          }
          return queryString;
        }
 
        var getSnappedCoordinates = function(queryString) {
          var queryString1 = "28.709861,77.176552|28.705344,77.185135|28.701429,77.200584|28.695707,77.211914|28.692997,77.22187|28.689985,77.22084|28.686371,77.221184|28.682757,77.222557|28.679143,77.2229|28.679143,77.228394|28.676432,77.230453|28.67101,77.230797|28.6686,77.233543|28.666491,77.235603|28.66378,77.237663|28.66137,77.243843|28.658056,77.247276|28.652031,77.252769|28.647511,77.253799|28.638472,77.257919|28.63576,77.254143|28.634856,77.24556|28.630637,77.24762|28.621597,77.248306|28.612857,77.250366|28.608034,77.252083|28.604417,77.252769|28.601403,77.254829|28.597183,77.256203|28.594169,77.256546|28.584522,77.261009|28.58422,77.264099|28.58211,77.266502|28.579397,77.267876|28.575477,77.263412|28.571859,77.256546|28.569145,77.254829|28.56613,77.253456";
          var queryString2 = "28.564924,77.24762|28.565527,77.238007|28.565829,77.225647|28.569145,77.222557|28.569748,77.213631|28.569748,77.206421|28.569145,77.195091|28.570351,77.182732|28.572462,77.177582|28.578191,77.176552|28.584823,77.172089|28.592058,77.168999|28.598087,77.163162|28.602307,77.156982|28.606527,77.14016|28.608938,77.138786|28.615569,77.137413|28.619788,77.13604|28.637568,77.130547|28.645402,77.12574|28.651428,77.12471|28.658056,77.125397|28.661972,77.13089|28.668299,77.13707|28.676733,77.141533|28.681251,77.14119|28.68366,77.145309|28.68607,77.151833|28.691792,77.153206|28.69631,77.156296|28.699622,77.156982|28.700827,77.163506|28.703236,77.167282|28.705645,77.172089|28.708957,77.176552|28.706247,77.181015|28.705645,77.185478|28.704139,77.188911|28.702032,77.194061|28.700827,77.199898|28.698719,77.204704|28.697213,77.211227|28.694653,77.214832|28.693599,77.217751|28.692846,77.220669|28.690964,77.221184|28.689006,77.221355|28.686296,77.22187|28.685129,77.221999|28.683924,77.222171|28.682757,77.222042|28.682117,77.222385|28.681665,77.2226|28.682042,77.223716|28.682418,77.224789|28.682042,77.226033|28.681853,77.22702|28.681063,77.227621|28.680159,77.228565|28.679896,77.228909|28.682192,77.229209|28.684526,77.228866|28.686258,77.228565|28.690061,77.227836|28.695105,77.227535|28.697289,77.227192|28.700225,77.227535|28.703048,77.227664";
          var queryString3 = "28.602157,77.134495|28.607431,77.121363|28.603927,77.112865|28.604794,77.110806|28.605435,77.109432|28.606301,77.107544|28.606527,77.106943|28.606753,77.106042|28.607356,77.104754|28.60811,77.102995|28.60875,77.101622|28.609278,77.100677|28.609391,77.099562|28.609051,77.097802|28.609278,77.0963|28.610031,77.09527|28.610747,77.09321|28.61135,77.091751|28.612103,77.090034|28.612518,77.088833|28.613196,77.087245|28.613761,77.085786|28.614627,77.084455|28.614966,77.083211|28.615494,77.082396|28.616059,77.081065|28.616436,77.080293|28.61685,77.079177|28.617377,77.078233|28.618018,77.076859|28.618282,77.076173|28.618809,77.075486|28.61911,77.074499|28.619826,77.073169|28.620354,77.072096|28.620655,77.071323|28.621898,77.069607|28.623028,77.068663|28.624422,77.067804|28.625439,77.067204|28.635007,77.062311|28.638811,77.060208|28.637756,77.058749|28.63802,77.057762|28.639564,77.056003|28.641711,77.055874|28.644122,77.056389|28.645779,77.055831|28.646306,77.055445|28.645496,77.054179|28.646589,77.052956|28.6456,77.053031|28.645609,77.051904|28.64463,77.051969|28.644724,77.051336|28.644131,77.051314|28.644188,77.050906|28.644668,77.050949|28.644724,77.050059|28.645769,77.050134|28.645779,77.049147|28.645911,77.039201|28.647059,77.039158|28.648359,77.039115|28.649319,77.039051|28.648434,77.036669|28.64672,77.03418";
          var queryString4 = "28.502243,77.185671|28.502319,77.186487|28.502262,77.187173|28.502337,77.187431|28.502526,77.188032|28.502394,77.188933|28.502432,77.18992|28.503393,77.190092|28.503846,77.190006|28.503827,77.188976|28.503167,77.188761|28.501715,77.188804|28.500489,77.188761|28.500508,77.18962|28.499829,77.189705|28.499735,77.18889|28.498887,77.188675|28.498415,77.188761|28.498472,77.190371|28.498491,77.191744|28.498623,77.192967|28.498868,77.193568|28.499377,77.193568|28.499735,77.194083|28.499961,77.194641|28.499716,77.195005|28.499339,77.19552|28.498962,77.195842|28.498321,77.196615";
          var apiKey = "AIzaSyAye_P1o92tyk_RBg7tP9SSzhrgfAO-qx4";
          var url = "https://roads.googleapis.com/v1/snapToRoads?path="+queryString1+"&key="+apiKey+"&interpolate=true";
          $.get(url, function(response) {
              processSnapToRoadResponse1(response);
 
              // This draws the route taken by the truck.
              drawSnappedPolyline("red",snappedCoordinates1);
 
              //This shows the marker(Truck) Movement in real time
              // animateTruck1();
 
 
          });
          //truck 2 qs
          // url = "https://roads.googleapis.com/v1/snapToRoads?path="+queryString2+"&key="+apiKey+"&interpolate=true";
          // $.get(url, function(response) {
          //     processSnapToRoadResponse2(response);
 
          //     // This draws the route taken by the truck.
          //     drawSnappedPolyline("blue",snappedCoordinates2);
 
          //     //This shows the marker(Truck) Movement in real time
          //     animateTruck2();
 
 
          // });
          // //truck 3 qs
          // url = "https://roads.googleapis.com/v1/snapToRoads?path="+queryString3+"&key="+apiKey+"&interpolate=true";
          // $.get(url, function(response) {
          //     processSnapToRoadResponse3(response);
 
          //     // This draws the route taken by the truck.
          //     drawSnappedPolyline("green",snappedCoordinates3);
 
          //     //This shows the marker(Truck) Movement in real time
          //     animateTruck3();
 
 
          // });
          // //truck 4 qs
          // url = "https://roads.googleapis.com/v1/snapToRoads?path="+queryString4+"&key="+apiKey+"&interpolate=true";
          // $.get(url, function(response) {
          //     processSnapToRoadResponse4(response);
 
          //     // This draws the route taken by the truck.
          //     drawSnappedPolyline("yellow",snappedCoordinates4);
 
          //     //This shows the marker(Truck) Movement in real time
          //     animateTruck4();
 
 
          // });
 
        }
 
        // Store snapped polyline returned by the snap-to-road method.
        function processSnapToRoadResponse1(data) {
          console.log(data);
          snappedCoordinates1 = [];
          placeIdArray = [];
          for (var i = 0; i < data.snappedPoints.length; i++) {
              var latlng = new google.maps.LatLng(
                  data.snappedPoints[i].location.latitude,
                  data.snappedPoints[i].location.longitude);
              snappedCoordinates1.push(latlng);
              placeIdArray.push(data.snappedPoints[i].placeId);
          }
        }
      //   function processSnapToRoadResponse2(data) {
      //     console.log(data);
      //     snappedCoordinates2 = [];
      //     placeIdArray = [];
      //     for (var i = 0; i < data.snappedPoints.length; i++) {
      //         var latlng = new google.maps.LatLng(
      //             data.snappedPoints[i].location.latitude,
      //             data.snappedPoints[i].location.longitude);
      //         snappedCoordinates2.push(latlng);
      //         placeIdArray.push(data.snappedPoints[i].placeId);
      //     }
      //   }
      //   function processSnapToRoadResponse3(data) {
      //     console.log(data);
      //     snappedCoordinates3 = [];
      //     placeIdArray = [];
      //     for (var i = 0; i < data.snappedPoints.length; i++) {
      //         var latlng = new google.maps.LatLng(
      //             data.snappedPoints[i].location.latitude,
      //             data.snappedPoints[i].location.longitude);
      //         snappedCoordinates3.push(latlng);
      //         placeIdArray.push(data.snappedPoints[i].placeId);
      //     }
      //   }
      //   function processSnapToRoadResponse4(data) {
      //     console.log(data);
      //     snappedCoordinates4 = [];
      //     placeIdArray = [];
      //     for (var i = 0; i < data.snappedPoints.length; i++) {
      //         var latlng = new google.maps.LatLng(
      //             data.snappedPoints[i].location.latitude,
      //             data.snappedPoints[i].location.longitude);
      //         snappedCoordinates4.push(latlng);
      //         placeIdArray.push(data.snappedPoints[i].placeId);
      //     }
      //   }
 
        // Draws the snapped polyline (after processing snap-to-road response).
        function drawSnappedPolyline(color,snap) {
          var snappedPolyline = new google.maps.Polyline({
              path: snap,
              strokeColor: color,
              strokeWeight: 2
          });

          polylines.push(snappedPolyline);
          snappedPolyline.setMap(map);

        }

      //   function animateTruck1(){
      //     // This is the function for moving the truck marker
      //     (function myLoop (i) {
      //         setTimeout(function () {
      //             marker1.setPosition(snappedCoordinates1[i]);
      //             if(i<snappedCoordinates1.length*3/4)
      //                                   marker1.setIcon(STATIC_URL + "fuel_tanker_red.png");
      //             if (--i) myLoop(i);
      //         }, 400)
      //     })(snappedCoordinates1.length);
      //   }
      //   function animateTruck2(){
      //     // This is the function for moving the truck marker
      //     (function myLoop (i) {
      //         setTimeout(function () {
      //             marker2.setPosition(snappedCoordinates2[i]);
      //             if (--i) myLoop(i);
      //         }, 400)
      //     })(snappedCoordinates2.length);
      //   }
      //   function animateTruck3(){
      //     // This is the function for moving the truck marker
      //     (function myLoop (i) {
      //         setTimeout(function () {
      //             marker3.setPosition(snappedCoordinates3[i]);
      //             if(i<snappedCoordinates3.length*3/4)
						// marker3.setIcon(STATIC_URL + "fuel_tanker_yellow.png");
      //             if (--i) myLoop(i);
      //         }, 400)
      //     })(snappedCoordinates3.length);
      //   }
      //   function animateTruck4(){
      //     // This is the function for moving the truck marker
      //     (function myLoop (i) {
      //         setTimeout(function () {
      //             marker4.setPosition(snappedCoordinates4[i]);
      //             if(i<snappedCoordinates4.length*3/4)
      //                                   marker4.setIcon(STATIC_URL + "fuel_tanker_yellow.png");
      //                                   if(i<snappedCoordinates4.length/4)
      //                                   marker4.setIcon(STATIC_URL + "fuel_tanker_red.png");
      //             if (--i) myLoop(i);
      //         }, 400)
      //     })(snappedCoordinates4.length);
      //   }
        getLocationDataForTanker();
});
