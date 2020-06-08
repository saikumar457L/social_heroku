(function() {
  if (window.myBookmarklet !== undefined){
    myBookmarklet();
  }
  else {
    document.body.appendChild(document.createElement('script')).src='https://9144288b5d42.ngrok.io/static/js/bookmarklet.js?r='+Math.floor(Math.random()*999);

  }
})();
