---
layout: default
---

# Data + tennis

I'm a lifelong tennis player and have stayed active in the game as a player, community organizer at the [Fort Greene Tennis Association](http://www.fortgreenetennis.org/), and through a side business with my friend called [Bageled NYC](https://bageled.nyc/). And in the Spring of 2022 I started working in tennis full time as a Data Engineer at [Universal Tennis](https://www.universaltennis.com/). 

At Universal Tennis, I keep our existing data pipelines running, build new pipelines for new products, and find ways to get involved any way I can in other aspects of the business. And here's a little bit about some of my personal projects with tennis and data:
<br>
<br>
## Bageled NYC

I'm working with a creative partner on a project called [Bageled NYC](https://www.bageled.nyc/), where we print and sell bagel-inspired grips for tennis rackets (in tennis, a score of 6-0 is also called a "bagel"). I've worked on everything from production sourcing to social media outreach. One of my main projects was to create our website, which has steadily evolved and now includes [a fun leaderboard](https://bageled.nyc/bagel-race) showing which pro tennis players currently have the most bagels on tour:
<br>
<br>
<a href="https://datastudio.google.com/reporting/02761227-2cfd-48d6-91e4-5b261788ef62">
   <img alt="Bagel Race" src="./assets/images/bagel-race.png">
</a>
<br>
<br>
To pull in the data for this leaderboard, I wrote a cloud-based Python script for scraping scores from pro tennis matches across the globe:
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
I'm looking forward to working on this project more.
<br>
<br>
## FGTA and NYC tennis

Since the onset of COVID-19, tennis has seen a [significant increase in participation](https://www.pbs.org/newshour/show/how-has-covid-9-impacted-tennis) across the US. That has been especially true at Fort Greene Park, where we had lines of 50+ people starting each morning at around 6:30am. 

We've seen more and more players coming out to Fort Greene for years, but I wanted to get some hard numbers to back up these observations. So I started collecting data from the courts, created a survey, and summarized the results in a tidy little [Data Studio report](https://datastudio.google.com/u/0/reporting/6520be9f-9cab-4426-8896-2ac97b74b574/page/hZ4vB) (our data collection and research is ongoing):
<div class="w3-container">
  <img src="./assets/images/fgta-report.gif" style="width:100%;cursor:zoom-in;border:5px solid white"
  onclick="document.getElementById('modal02').style.display='block'">
  <div id="modal02" class="w3-modal" onclick="this.style.display='none'">
    <span class="w3-button w3-hover-yellow w3-xlarge w3-display-topright">X</span>
    <div class="w3-modal-content w3-animate-zoom">
      <img src="./assets/images/fgta-report.gif" style="width:100%">
    </div>
  </div>
</div>
<br>
To try and help distribute the demand for court time, I decided to make a map of tennis courts to help people find more places to play. So with a little Python, some NYC Open Data, and a dash of Google Maps results, we came up with [a map](http://www.fortgreenetennis.org/nyc-courts) of public and private tennis courts in NYC along with handball walls (they're great for practice!):

<div class="w3-container">
  <img src="./assets/images/tennis-map.gif" style="width:100%;cursor:zoom-in"
  onclick="document.getElementById('modal01').style.display='block'">
  <div id="modal01" class="w3-modal" onclick="this.style.display='none'">
    <span class="w3-button w3-hover-yellow w3-xlarge w3-display-topright">X</span>
    <div class="w3-modal-content w3-animate-zoom">
      <img src="./assets/images/tennis-map.gif" style="width:100%">
    </div>
  </div>
</div>
<br>
<br>
## ATP tennis

I'm also generally curious to know more about life on the ATP tour, especially when it comes to the financial aspects of that lifestyle. To figure out which players are making bank, who's breaking even, and who's in the red, I found prize money data from 2019 in PDF format, transformed thousands of those PDF pages into a table using Python, and analyzed the data using SQL. Here are a couple early findings:
<br>
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