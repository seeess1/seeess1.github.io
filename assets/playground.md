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
    <style>body {
  cursor: url('./images/cursor.png'), default;
}
a:link {
  cursor: url('./images/cursor.png');
}
a:visited {
  cursor: url('./images/cursor.png');
}</style>
<script> 
window.onkeydown = function( event ) {
    if ( event.keyCode == 27 ) {
        document.getElementsByClassName("w3-container").style.display="none"}
      };
</script>
</head>
# Playground

## Modal images

12:28 update

Modal:
<br>      
<div class="w3-container">
  <img src="./images/cocktails-smartphone.png" style="width:100%;cursor:zoom-in"
  onclick="document.getElementById('modal01').style.display='block'">
  <div id="modal01" class="w3-modal" onclick="this.style.display='none'">
    <span class="w3-button w3-hover-yellow w3-xlarge w3-display-topright">X</span>
    <div class="w3-modal-content w3-animate-zoom">
      <img src="./images/cocktails-smartphone.png" style="width:100%">
    </div>
  </div>  
</div>
<br>
<br>      
<div class="w3-container">
  <img src="./images/pie-earnings.png" style="width:100%;cursor:zoom-in"
  onclick="document.getElementById('modal02').style.display='block'">
  <div id="modal02" class="w3-modal" onclick="this.style.display='none'">
    <span class="w3-button w3-hover-yellow w3-xlarge w3-display-topright">X</span>
    <div class="w3-modal-content w3-animate-zoom">
      <img src="./images/pie-earnings.png" style="width:100%">
    </div>
  </div>  
</div>
<br>
<br>
Here's the code:
<br>
```js
<div class="w3-container">
  <img src="./images/cocktails-smartphone.png" style="width:100%;cursor:zoom-in"
  onclick="document.getElementById('modal01').style.display='block'">
  <div id="modal01" class="w3-modal" onclick="this.style.display='none'">
    <span class="w3-button w3-hover-yellow w3-xlarge w3-display-topright">X</span>
    <div class="w3-modal-content w3-animate-zoom">
      <img src="./images/cocktails-smartphone.png" style="width:100%">
    </div>
  </div>
  <script> 
window.onkeydown = function( event ) {
    if ( event.keyCode == 27 ) {
        document.getElementById('modal01').style.display='none’
    }
};
</script>
</div>

```

Any ideas?