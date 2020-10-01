---
layout: default
---

# Data engineering

Up until September 2020, I was a data engineer at a Brooklyn-based startup called [Topos](https://topos.com/). At Topos, our goal was to help business owners figure out where to expand to. For example, let's say you own a couple bars in the Grant Park neighborhood of Atlanta, GA and you want to open a new location in an entirely new city: Chicago, IL. But you have no idea which part of Chicago would be the best place for your business. 

Enter Topos. We would give you ranked recommendations for specific sections of particular neighborhoods in Chicago where you'd be most likely to find your target market:

![Neighborhoods in Chicago similar to Grant Park in Atlanta](https://github.com/seeess1/seeess1.github.io/raw/master/assets/images/atlanta-chicago.png)

And we'd do that by using data from a bunch of different places - like demographic stats from the US Census, the locations of all businesses across the country, vehicular traffic counts per hour per road segment for the entire US, restaurant reviews, and a lot more - and then feeding that data into our recommendation algorithm.

My job as a data engineer was to collect all the data feeding our algorithm, clean it, and generate new metrics from the raw data for our data science and front end teams to use. I wish I could share examples of the code here but I can't. But what I can say is that my job consisted of a lot of Python scripting to pull down data and load it into BigQuery (we primarily used Google Cloud products) and then SQL to clean and transform the data.

# Then COVID-19 happened

...and retail expansion collapsed. But we wanted to make the best use of our time so we built a [COVID-19 tracker](https://covid19.topos.com/):

![COVID-19 Tracker](https://github.com/seeess1/seeess1.github.io/raw/master/assets/images/covid.png)

I liked this project because it was relevant and fast-paced and because I got to lead the data engineering on it (again, lots of Python scripting plus SQL). My colleagues and I analyzed the data to look for insightful patterns and I became mostly interested in the economic effects of the disease. I created new pipelines to ingest decades of economic data from the Dept. of Labor, American Bankruptcy Institute, and the US Census and then used DataStudio to look for interesting trends like this one, which shows the total number of new businesses created each week for each state since the beginning of 2020 (my takeaway - there's more economic activity at least by one measure than one might expect, given unemployment figures this year):

![Business Filings](https://github.com/seeess1/seeess1.github.io/raw/master/assets/images/new-biz.png)

# In sum

My forte is in working with large geospatial data sets and knowing how to extract value from that data and extrapolate it to different geographic regions. But I also enjoy working with data of all types.