function getAway() {
  // Get away right now
  window.open("https://weather.com", "_newtab");
  // Replace current site with another benign site
  try { window.location.replace("http://google.com"); } 
    catch(e) { window.location = "http://google.com"; }
}

$(function() {

  $("#get-away").on("click", function(e) {
    getAway();
  });

  $("#get-away a").on("click", function(e) {
    // allow the (?) link to work
    e.stopPropagation();
  });

  $(document).keyup(function(e) {
    if (e.keyCode == 27) { // escape key
      getAway();
    }
  });

});
