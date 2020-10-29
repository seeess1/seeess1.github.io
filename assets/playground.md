---
layout: default
---
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="shortcut icon" type="image/x-icon" href="../assets/images/favicon-v6.ico">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=DM Sans">
    <link rel="stylesheet" href="./css/w3-mod.css">
    <style>* {
  cursor: url('./images/cursor.png'), auto;
}
a {
  cursor: url('./images/cursor.png');
}
img:hover{
  cursor: url('./images/cursor.png'); 
}
img{
  cursor: url('./images/cursor.png'); 
}
.w3-container{
  cursor: url('./images/cursor.png'); 
}
    li{
        cursor: pointer;
    }
</style>
<script> 
window.onkeydown = function( event ) {
    if ( event.keyCode == 27 ) {
        document.getElementsByClassName("w3-container").style.display="none"}
      };
</script>
</head>
<body>
# Playground

5:19 update

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
</body>