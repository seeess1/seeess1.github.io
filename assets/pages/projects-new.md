---
layout: default
---
<h1>Modal testing</h1>
<br>
I'm playing around with modal images but I noticed that my current method is shrinking the images. I'm guessing this is happening because I'm referencing this stylesheet: https://www.w3schools.com/w3css/4/w3.css. But I'm not sure how to fix it. Here's what I mean:
<h2>Normal/non-modal image</h2>
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
<h2>Solution?</h2>
How do I make it so that the modal image stretches all the way across?

P.S. How can I make the "x" in the close button of the modal image larger? I tried to control that in the style.scss file under the ".close" element but I don't think it changed anything.

P.P.S. How can I make the modal also respond to the escape key? So if someone wants to close the image, they can just hit escape and it will close out.