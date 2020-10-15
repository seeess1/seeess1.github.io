---
layout: default
---
<style>
* {
  font-family: 'DM Sans';
  color: #006600;
  background-color:#ffffff;
}
h1 {
  color: #006600;
  font-size: 30px;
  font-weight: bold;
}
h2 {
  color: #006600;
  font-size: 25px;
  font-weight: bold;
}
h3 {
  color: #006600;
  font-weight: bold;
  font-size: 20px;
}
body {
 font-size: 18px;
 color: #006600;
 background-color:#ffffff;
}
a:link {
  color: #696969;
}
a:visited {
  color: #696969;
}
</style>
<h1>Intro</h1>

I'm a data engineer (one half of my brain) who can also organize teams and projects (the other half).
<br>
<br>
<h2>The data half</h2>

I like Python, SQL, and maps (plus the occasional web development - like this website, for example).
<br>
<br>
<h3><a href="./projects">Projects</a></h3>

Many of <a href="./projects">my projects</a> center around making maps using geospatial data, like this COVID-19 tracker:

<a href="./projects"><img src="assets/images/covid-map.gif" alt="COVID-19 Tracker"></a>
<br>
<br>
<h3><a href="./data-and-tennis">Data + tennis</a></h3>

But I'm also in a long-term, committed relationship with tennis and I've <a href="./data-and-tennis">found ways</a> to combine that with data:

<a href="./data-and-tennis"><img src="assets/images/tennis-map.gif" alt="NYC Tennis Courts"></a>
<br>
<br>
<h2>The organizational half</h2>

Along with data engineering and analysis, I've also been a board member at a non-profit in Brooklyn since 2015. I explain the two halves in more detail <a href="./bio">here</a>.

<h1>Playing around with modals</h1>h1>
<div class="w3-container">
  <h2>W3.CSS Modal</h2>
  <button onclick="document.getElementById('id01').style.display='block'" class="w3-button w3-black">Open Modal</button>

  <div id="id01" class="w3-modal">
    <div class="w3-modal-content">
      <div class="w3-container">
        <span onclick="document.getElementById('id01').style.display='none'" class="w3-button w3-display-topright">&times;</span>
        <p>Some text. Some text. Some text.</p>
        <p>Some text. Some text. Some text.</p>
      </div>
    </div>
  </div>
</div>