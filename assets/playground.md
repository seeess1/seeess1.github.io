---
layout: default
---
  <head>
    <style>* {
  cursor: url('./images/cursor.png'), url('./images/cursor-2.png'), auto;
}
a {
  cursor: url('./images/cursor-2.png');
}
img:hover{
  cursor: url('./images/cursor-2.png'); 
}
img{
  cursor: url('./images/cursor-2.png'); 
}
.w3-container{
  cursor: url('./images/cursor-2.png'); 
}
    li{
        cursor: url('./images/cursor-2.png');
    }
</style>
</head>
# Playground

5:56 update

## Cursor

Here's <a href="./projects">a link</a>.

And here's an image:

<div class="w3-container">
  <img src="./images/cases.gif" style="width:100%;cursor:zoom-in"
  onclick="document.getElementById('modal01').style.display='block'">
  <div id="modal01" class="w3-modal" onclick="this.style.display='none'">
    <span class="w3-button w3-hover-yellow w3-xlarge w3-display-topright">X</span>
    <div class="w3-modal-content w3-animate-zoom">
      <img src="./images/cases.gif" style="width:100%">
    </div>
  </div>
</div>
And here's a list:
<ul>
  <li>List item one</li>
  <li>List item two</li>
  <li>List item three</li>
</ul>


## Modal images

Still need to figure out how to add the close-out functionality to the exit buttons.
<!-- <script> 
window.onkeydown = function( event ) {
    if ( event.keyCode == 27 ) {
        document.getElementsByClassName("w3-container").style.display="none"}
      };
</script> -->
