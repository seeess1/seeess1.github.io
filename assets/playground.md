---
layout: default
---
# Playground

## Modal images

1:02 update

Modal:
<br>
      <script> 
window.onkeydown = function( event ) {
    if ( event.keyCode == 27 ) {
        document.getElementById('modal01').style.display='none’
    }
};
</script>
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