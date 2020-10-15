---
layout: default
---
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">

<h1>Modal testing</h1>
<br>
<br>
<h2>Normal image</h2>
This image spans all the way from the left margin of the text to the right margin of the text. I think it looks nice this way.
<br>
<br>
<a href = "../images/reservations.png"><img src="../images/reservations.png" alt="Cocktails To Go"></a>
<br>
<br>
<h2>Modal image</h2>
This modal image pops out, which is nice. But it doesn't span all the way from the left text margin to the right text margin. It's slightly shrunken.
<br>
<br>
<div class="w3-container">
  <img src="../images/reservations.png" style="width:100%;cursor:zoom-in"
  onclick="document.getElementById('modal01').style.display='block'">

  <div id="modal01" class="w3-modal" onclick="this.style.display='none'">
    <span class="w3-button w3-hover-red w3-xlarge w3-display-topright">&times;</span>
    <div class="w3-modal-content w3-animate-zoom">
      <img src="../images/reservations.png" style="width:100%">
    </div>
  </div>
</div>