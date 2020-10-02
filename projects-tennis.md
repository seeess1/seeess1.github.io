---
layout: default
---

![Brooklyn tennis permits](https://github.com/seeess1/seeess1.github.io/raw/master/assets/images/brooklyn-permits.png)


# Data + tennis

I've done side projects combining tennis and data for fun and to help out with our non-profit work at the [Fort Greene Tennis Association](http://www.fortgreenetennis.org/). 

## Fun

My friend Michael and I created bagel-themed grips for tennis rackets. Michael is the mastermind behind the concept and artwork. I put together our website, which includes scores from pro tennis matches across the globe that I scrape via a cloud-based Python script I wrote. 

```python
def bagel_finder():
    # Iterate through pro matches
    for match in loaded_json["results"]:                
            # Get the match score as a string
            match_score = ""
            set_scores = match["sport_event_status"]["period_scores"]
            # Iterate through sets in the match
            for set_score in set_scores:                
                    match_score += str(set_score["home_score"]) + " - " + str(set_score["away_score"]) + " "
```

I enjoy this.

![Bageled](https://github.com/seeess1/seeess1.github.io/raw/master/assets/images/bageled.png)

## NYC tennis

I created the map at the top of this page using tennis permit purchase data that I FOIA requested from the NYC Parks Department. And this chart visualizing trends in permit purchases among different age groups:

![Tennis permits age groups](https://github.com/seeess1/seeess1.github.io/raw/master/assets/images/permits-age.png)

The point of all of this work is to understand the degree to which tennis is growing in NYC and where. The work is ongoing.

## ATP tennis

And I've taken a look at earnings on the ATP Tour to understand which players are making bank, who's breaking even, and who's in the red since life on the pro tour is apparently rather expensive. This project involved parsing thousands of pages of PDFs using Python into a machine-readable table and then some analysis in SQL. Here are a couple findings:

![Ranking groups](https://github.com/seeess1/seeess1.github.io/raw/master/assets/images/ranking-groups.png)
Players in the top 20 did, in fact, make bank in 2019. And then weekly earnings drop off a cliff, which is a problem for the lower ranks since it apparently costs around $3k per week just to compete on the tour.

![Pie of earnings](https://github.com/seeess1/seeess1.github.io/raw/master/assets/images/ranking-groups.png)
In 2019, there was $230,506,600 in total prize money up for grabs. So we're seeing that ATP players in the top 100 captured 78% of that prize money. The other 22% was divided up among 400+ players.