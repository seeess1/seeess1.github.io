---
layout: default
---
# Playground

## Modal images

Right now my modal image pops out, which is some progress.
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
Now I'd like to make it so that users can exit out of the pop up by hitting the escape key. I found [this on stackoverflow](https://stackoverflow.com/questions/1481626/how-to-handle-esc-keydown-on-javascript-popup-window) but I'm not sure how I would incorporate it into my code:

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
</div>
```

Any ideas?