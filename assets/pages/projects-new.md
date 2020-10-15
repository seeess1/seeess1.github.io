---
layout: default
---
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">

<h1>Data engineering</h1>

Up until September 2020, I was a data engineer at a Brooklyn-based startup called [Topos](https://topos.com/), where we specialized in making maps. 
<br>
<br>
To make our maps, we needed lots of data: demographic stats from the Census, business metadata, vehicular traffic counts, restaurant reviews, and much more. The data I collected, cleaned, and transformed served as the backbone for our applications, including...
<br>
<br>
<h2>COVID-19 Compiler</h2>
In Spring 2020 we built a [COVID-19 tracker](https://covid19.topos.com/), which lets users explore different ways to measure COVID-19 cases in the US:

<a href = "../images/cases.gif"><img src="../images/cases.gif" alt="COVID-19 Tracker"></a>
<br>
<br>
<div class="w3-container">
  <img src="../images/cases.gif" style="width:100%;cursor:zoom-in"
  onclick="document.getElementById('modal01').style.display='block'">

  <div id="modal01" class="w3-modal" onclick="this.style.display='none'">
    <span class="w3-button w3-hover-red w3-xlarge w3-display-topright">&times;</span>
    <div class="w3-modal-content w3-animate-zoom">
      <img src="../images/cases.gif" style="width:100%">
    </div>
  </div>
</div>

It also lets users layer demographic stats (like population, unemployment numbers, and housing density) on top of case counts to look for interesting overlaps:

<a href = "../images/layers.gif"><img src="../images/layers.gif" alt="Layering stats"></a>
<br>
<br>
## Retail

We helped retailers decide how to grow their business by making maps like this one, which finds similar neighborhoods across cities based on machine learning models:

<a href = "../images/neighborhoods.gif"><img src="../images/neighborhoods.gif" alt="Neighborhoods gif"></a>
<br>
<br>
## Cocktails To Go

And we even made maps for New Yorkers looking for [a place to get a drink outside](https://cocktails.topos.com/):

<a href = "../images/cocktails-smartphone.png"><img src="../images/cocktails-smartphone.png" alt="Cocktails To Go"></a>
<br>
<br>
# Data analysis

When I wasn't transforming large data sets, I did my own analysis for Topos on topics like [trends in job postings nationwide](https://twitter.com/topos_ai/status/1258184297732849666) following the onset of COVID-19. Or looking at communities in the American Southwest that are particularly vulnerable to [public health crises](https://medium.com/topos-ai/high-covid-19-vulnerability-seen-in-and-near-navajo-nation-and-hopi-reservation-in-arizona-edba321699cb):

<a href = "../images/reservations.png"><img src="../images/reservations.png" alt="COVID-19 cases in the American Southwest"></a>
<br>
<br>
# Data science

And before joining Topos, I cut my teeth with data engineering, mapping, and analysis at NYU in an [applied data science program](https://cusp.nyu.edu/). My projects included: 
* [Anomaly detection](https://github.com/seeess1/machineLearning/blob/master/anomalies_traffic_health.ipynb) in traffic data
* Analyzing the relationship between [bars and 311 complaints](https://github.com/seeess1/publicDrunkenness/blob/master/public_drunkenness.ipynb)
* [LiDAR mapping](https://sketchfab.com/3d-models/nyu-cusp-lidar-exercise-a5b41ceffb5f47f8a9c11123de2f20ea)
* [Using computer vision](https://github.com/seeess1/pedestrian_cv) to count pedestrians at an intersection on campus:
<br>
<br>
<a href = "../images/pedestrians.png"><img src="../images/pedestrians.png" alt="Computer vision"></a>

Plus exercises in [streaming big data](https://github.com/seeess1/bigData) and more [machine learning](https://github.com/seeess1/machineLearning).
<br>
<br>
# Data + tennis

I also look for projects that combine programming with my non-profit work and general interest in tennis. You can learn more about these projects <a href="./data-and-tennis">here</a>.