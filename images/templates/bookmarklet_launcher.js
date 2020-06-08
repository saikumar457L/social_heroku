(function() {
  if (window.myBookmarklet !== undefined){
    myBookmarklet();
  }
  else {
    document.body.appendChild(document.createElement('script')).src='https://warm-stream-62067.herokuapp.com/static/js/bookmarklet.js?r='+Math.floor(Math.random()*999);

  }
})();
