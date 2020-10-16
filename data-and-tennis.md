---
layout: default
---

# Data + tennis

I've come up with self-directed projects combining tennis and data to help with my work as a board member at the [Fort Greene Tennis Association](http://www.fortgreenetennis.org/), as part of an entrepreneurial project my friend and I started, and out of general curiosity. 
<br>
<br>
## FGTA and NYC tennis

Data is playing a bigger role at the Fort Greene Tennis Association than ever before and I've spearheaded several related projects. 
<br>
<br>
To help people find places to play racket sports in NYC, I collected data with the location of every handball wall and public tennis court in NYC and used Python to clean it and geocode the addresses. Then I worked with a colleague to [map them](http://www.fortgreenetennis.org/nyc-courts):

<div class="w3-container">
  <img src="./assets/images/tennis-map.gif" style="width:100%;cursor:zoom-in"
  onclick="document.getElementById('modal01').style.display='block'">
  <div id="modal01" class="w3-modal" onclick="this.style.display='none'">
    <span class="w3-button w3-hover-yellow w3-xlarge w3-display-topright">X</span>
    <div class="w3-modal-content w3-animate-zoom">
      <img src="./assets/images/tennis-map.gif.png" style="width:100%">
    </div>
  </div>
</div>
<br>
<br>
I've also analyzed tennis permit sales by zip code using data I FOIL requested from the NYC Parks Department:

<div class="w3-container">
  <img src="./assets/images/geo-viz.png" style="width:100%;cursor:zoom-in"
  onclick="document.getElementById('modal02').style.display='block'">
  <div id="modal02" class="w3-modal" onclick="this.style.display='none'">
    <span class="w3-button w3-hover-yellow w3-xlarge w3-display-topright">X</span>
    <div class="w3-modal-content w3-animate-zoom">
      <img src="./assets/images/geo-viz.png" style="width:100%">
    </div>
  </div>
</div>
<br>
<br>
And visualized trends in permit purchases among different age groups using the same data set from NYC Parks:

<div class="w3-container">
  <img src="./assets/images/permits-age.png" style="width:100%;cursor:zoom-in"
  onclick="document.getElementById('modal03').style.display='block'">
  <div id="modal03" class="w3-modal" onclick="this.style.display='none'">
    <span class="w3-button w3-hover-yellow w3-xlarge w3-display-topright">X</span>
    <div class="w3-modal-content w3-animate-zoom">
      <img src="./assets/images/permits-age.png" style="width:100%">
    </div>
  </div>
</div>
<br>
<br>
The point of all of this work is to understand the degree to which tennis is growing in NYC and to help meet the demand for tennis in the City (which is on the rise). The work is ongoing...
<br>
<br>
## Bageled NYC

I'm working with a creative partner on producing bagel-themed grips for tennis rackets (in tennis, a score of 6-0 is also called a "bagel"). To showcase our product, I created [our website](https://www.bageled.nyc/), which includes a cloud-based Python script for scraping scores from pro tennis matches across the globe:

```python
def score_analyzer():
    # Iterate through pro matches
    for match in api_json["results"]:                
            # Save the match score as a string
            match_score = ""
            set_scores = match["sport_event_status"]["period_scores"]
            # Iterate through sets in the match
            for set_score in set_scores:                
                    match_score += str(set_score["home_score"]) + \
                    " - " + str(set_score["away_score"]) + " "
```

<div class="w3-container">
  <img src="./assets/images/bageled.png" style="width:100%;cursor:zoom-in"
  onclick="document.getElementById('modal04').style.display='block'">
  <div id="modal04" class="w3-modal" onclick="this.style.display='none'">
    <span class="w3-button w3-hover-yellow w3-xlarge w3-display-topright">X</span>
    <div class="w3-modal-content w3-animate-zoom">
      <img src="./assets/images/bageled.png" style="width:100%">
    </div>
  </div>
</div>
<br>
I'm looking forward to working on this project more.
<br>
<br>
## ATP tennis

I'm also generally curious to know more about life on the ATP tour, especially when it comes to the financial aspects of that lifestyle. To figure out which players are making bank, who's breaking even, and who's in the red, I found prize money data from 2019 in PDF format, transformed thousands of those PDF pages into a table using Python, and analyzed the data using SQL. Here are a couple early findings:
<br>
### Weekly earnings

<div class="w3-container">
  <img src="./assets/images/ranking-groups.png" style="width:100%;cursor:zoom-in"
  onclick="document.getElementById('modal05').style.display='block'">
  <div id="modal05" class="w3-modal" onclick="this.style.display='none'">
    <span class="w3-button w3-hover-yellow w3-xlarge w3-display-topright">X</span>
    <div class="w3-modal-content w3-animate-zoom">
      <img src="./assets/images/ranking-groups.png" style="width:100%">
    </div>
  </div>
</div>
<br>

Pictured above are the weekly earnings for different groups of ranked players. My analysis showed that players in the top 20 did, in fact, make bank in 2019. But then weekly earnings drop off a cliff, which is a problem for the lower ranks since it apparently costs around $3k per week just to compete on the tour.
<br>

### Total prize money pot

<div class="w3-container">
  <img src="./assets/images/pie-earnings.png" style="width:100%;cursor:zoom-in"
  onclick="document.getElementById('modal06').style.display='block'">
  <div id="modal06" class="w3-modal" onclick="this.style.display='none'">
    <span class="w3-button w3-hover-yellow w3-xlarge w3-display-topright">X</span>
    <div class="w3-modal-content w3-animate-zoom">
      <img src="./assets/images/pie-earnings.png" style="width:100%">
    </div>
  </div>
</div>
<br>

This is a snapshot of which players took home the most money out of the pot of total prize money in 2019.
That year, there was $230,506,600 in total prize money up for grabs. So we're seeing that ATP players in the top 100 captured 78% of that prize money while the other 22% was divided up among 400+ players.

[Reach out](./contact.md) if you've got suggestions or wanna collaborate.