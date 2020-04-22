Title: Data Science and PAW Patrol
Date: 2020-04-22 12:00
Status: published
Category: fun
Tags: family, data science, 8 minute read
Slug: paw-patrol
Authors: Philip Shemella
Summary: A fun look at PAW Patrol's effect on pet naming

## Step 0. The disclaimers

1. I don't call myself a _data scientist_, but other people do, and I wanted to share my approach to _data science_. This approach has worked well for me professionally. There are many good approaches, and I don't want to gatekeep any of those.

2. PAW Patrol is a registered trademark of someone else. I don't own any rights to PAW Patrol. If I did, I would be doing something better with my free time.

## Step 1. Start with the science

Thinking like a scientist means having a question, and then searching out an answer. Science isn't data-driven, in that the data can provide an answer, but the available data shouldn't suggest the question. At least in most of the cases I can think of.

This is a huge challenge to productionalize data science in a business environment. With a recent (unnamed) employer, we had a big data-engineering effort to rebuild an analysis pipeline. As an analyst, it became slowly clear that with the new pipeline, we could only recreate 5 of the 6 key metrics. I left the company before the proposed workaround was implemented.

For my example of methodology, I'll use [PAW Patrol](https://en.wikipedia.org/wiki/PAW_Patrol). It's a kids' animated TV series. To describe cast of characters, and the _plot_, here are the lyrics to the theme song:

> <sub>PAW Patrol, PAW Patrol</sub>

> <sub>We'll be there on the double</sub>

> <sub>Whenever there's a problem</sub>

> <sub>'Round Adventure Bay</sub>

> <sub>Ryder and his team of pups</sub>

> <sub>Will come and save the day</sub>

> <sub>Marshall, Rubble, Chase</sub>

> <sub>Rocky, Zuma, Skye</sub>

> <sub>Yeah! They're on the way!</sub>

Yeah. It goes on. You get the point. But the show can be endearing, and I think the deeper reason it resonates with kids is because the team is useful and appreciated by the adults they help. But that's a topic for another article.<sup>
[1]</sup>

If you take a vote in my household, a consensus of 50% of voters will declare PAW Patrol to be the single best achievement of humanity. And it's been decided, by compromise, that if we ever get a pet dog, the name shall be either `Zuma-Marshall`, or `Marshall-Zuma`.

![paw patrol team]({attach}/images/paw-patrol-jump-i49016.jpg)

### The question

I was curious - with PAW Patrol hype slowly sweeping the planet since 2013, do we see an increase in dogs named after the crew?

## Step 2. Curate the data

I need open data with pet names. Dog names. There are several, and I'll outline why they make a good or bad candidate for the analysis.

### [Hundenamen aus dem Hundebestand der Stadt Zürich](https://data.stadt-zuerich.ch/dataset/sid_stapo_hundenamen)

This one is from the city of Zürich, Switzerland, where I live. I've seen a [recent Twitter post](https://twitter.com/OpenDataZurich/status/1235887129047240704) about this dataset, so that may have planted the idea that dog names can be open data.

Data goes back to 2015, and each year is one CSV file. To get an idea of the dataset size, I choose the complete year of [2019](https://data.stadt-zuerich.ch/dataset/sid_stapo_hundenamen/resource/37af5c6e-c101-41aa-8072-033280191f9c). 7647 records. It may be hard to find trends in so few dog registrations. Additionally, the Paw Patrol trend is slowly making it here to Switzerland. Since it started in North America, I'll go to look there.

### [Anchorage Dog Names over Time](https://catalog.data.gov/dataset/dog-names-over-time)

Only 16k total names between 2017 and 2019. That's not enough dogs when there are so many possible names. And starting in 2017, I may not get a good _before_ snapshot.

### [Seattle Pet Licenses](https://catalog.data.gov/dataset/seattle-pet-licenses)

> A list of active/current Seattle pet licenses, including animal type (species), pet's name, breed and the owner's ZIP code.

This might be a good dataset because records go back to 2000 and are updated through 2019. I can get snapshots before and during the PAW Patrol era. But I counted dogs registered in 2019 and it was 11k. In 2018, 7k. Still not enough.

### [NYC Dog Licensing Dataset](https://data.cityofnewyork.us/Health/NYC-Dog-Licensing-Dataset/nu7n-tubp)

This could be it. Recently updated. 24.1 MB CSV file. 345k total rows going back more than 10 years. 79k dog registrations in 2019. Explore the data [here](https://data.cityofnewyork.us/Health/NYC-Dog-Licensing-Dataset/nu7n-tubp/data).

The fine print:

> _Each record stands as a unique license period for the dog over the course of the yearlong time frame._

What does this mean for my data? It means that dog names are assigned at least once per year. If I count unique dog names over multiple years, I'll be over counting. 

and

> _Each record represents a unique dog license that was active during the year, but not necessarily a unique record per dog, since a license that is renewed during the year results in a separate record of an active license period._

This means that dog-names within a given year may actually be duplicate as well. If this was a real project, in order to fully trust my data, I would first count how many names are repeated. To do this, because there is no column `dog ID` which would uniquely identify a dog, I would have to create a surrogate key based on the columns such as `AnimalBirthMonth`, `AnimalGender` and `BreedName`, and perhaps also the geographical data `Borough` and `ZipCode`.

If I cared more about Paw Patrol pet-naming theory, I could build a unified dog-name data-model and combine datasets, and keep looking for new sources to add. But I don't care that much. On to the answer. Let's hope NYC is a trend-setter -- when it comes to naming pets after kids' cartoon superheros.

## Step 3. Explore the data

Lots of tools but because I _know_ that I won't productionalize this pipeline, I'm going to dump the data into the commercial BI tool Tableau Desktop. Licenses are expensive, and there are many solid open source tools that will do the job. But the software allows me to do fast visual anaylsis. If you sign up for the [free audit of this Coursera](https://www.coursera.org/learn/analytics-tableau), you'll see that after clicking through the 3rd week or so, you are provided a 6-month software license to complete the rest of the course. _YMMV._

### Visual Analysis

In this step, I'm trying to get a feel for the data. Is it clean, is it reliable? Will it answer my question?

What are the 5 most common names for dogs in NYC? 

<sub>Name</sub>|<sub>Frequency</sub>
:-------------|:-------------:
<sub>UNKNOWN</sub>|<sub>5379</sub>
<sub>BELLA</sub>|<sub>3824</sub>
<sub>NAME NOT PROVIDED</sub>|<sub>3763</sub>
<sub>MAX</sub>|<sub>3582</sub>
<sub>CHARLIE</sub>|<sub>2852</sub>
<sub>COCO</sub>|<sub>2636</sub>

Woof. That's a lot of _NULL_. Let's see how it's evenly distributed throughout the years

<sub>AnimalName</sub> | <sub>2014</sub> | <sub>2015</sub> | <sub>2016</sub> | <sub>2017</sub> | <sub>2018</sub>
:---|:---:| :---: | :---: | :---: | :---:
<sub>UNKNOWN</sub> | <sub>3</sub> | <sub>1179</sub> | <sub>1903</sub> | <sub>1294</sub> | <sub>1000</sub>
<sub>BELLA</sub> | <sub>19</sub> | <sub>427</sub> | <sub>1332</sub> | <sub>1233</sub> | <sub>813</sub>
<sub>NAME NOT PROVIDED</sub> | <sub>11</sub> | <sub>963</sub> | <sub>1374</sub> | <sub>847</sub> | <sub>568</sub>
<sub>MAX</sub> | <sub>34</sub> | <sub>444</sub> | <sub>1214</sub> | <sub>1166</sub> | <sub>724</sub>
<sub>CHARLIE</sub> | <sub>26</sub> | <sub>293</sub> | <sub>1027</sub> | <sub>935</sub> | <sub>571</sub>
<sub>COCO</sub> | <sub>22</sub> | <sub>296</sub> | <sub>941</sub> | <sub>817</sub> | <sub>560</sub>

OK, better. It seems pretty flat, except for 2014. Let's do a quick check of total names per year, to see that indeed 2014 has many fewer.

<sub>Year of LicenseIssuedDate</sub>|<sub>Frequency</sub>
:--- | :---:
<sub>2014</sub>|<sub>2650</sub>
<sub>2015</sub>|<sub>42439</sub>
<sub>2016</sub>|<sub>119080</sub>
<sub>2017</sub>|<sub>110995</sub>
<sub>2018</sub>|<sub>70563</sub>

Bummer that 2019 registrations aren't there yet. I hope NYC is trend-setting enough to show a signal in 2018.

Another learning is that we should exclude 2014 from the calculation -- there are just not enough records, especially in comparison with other years.

### Initial Calculation

I want to start to measure trends, and I'll do so visually, since I need to only compare a handful of names.

Marshall, Rubble, Chase, Rocky, Zuma and Skye. Let's add Ryder, even though he is a human in the cartoon. And the pups added in later seasons: Everest and Tracker.

<sub>AnimalName</sub> | <sub>2014</sub> | <sub>2015</sub> | <sub>2016</sub> | <sub>2017</sub> | <sub>2018</sub>
:---|:---:|:---:|:---:|:---:|:---:
<sub>CHASE</sub> | <sub>7</sub> | <sub>49</sub> | <sub>115</sub> | <sub>170</sub> | <sub>86</sub>
<sub>EVEREST</sub> | <sub></sub> | <sub>1</sub> | <sub>9</sub> | <sub>5</sub> | <sub>3</sub>
<sub>MARSHALL</sub> | <sub></sub> | <sub>7</sub> | <sub>26</sub> | <sub>19</sub> | <sub>11</sub>
<sub>ROCKY</sub> | <sub>20</sub> | <sub>300</sub> | <sub>823</sub> | <sub>785</sub> | <sub>486</sub>
<sub>RUBBLE</sub> | <sub></sub> | <sub></sub> | <sub></sub> | <sub>6</sub> | <sub>2</sub>
<sub>RYDER</sub> | <sub></sub> | <sub>13</sub> | <sub>28</sub> | <sub>26</sub> | <sub>18</sub>
<sub>SKYE</sub> | <sub></sub> | <sub>10</sub> | <sub>61</sub> | <sub>54</sub> | <sub>36</sub>
<sub>TRACKER</sub> | <sub></sub> | <sub></sub> | <sub></sub> | <sub></sub> | <sub>1</sub>
<sub>ZUMA</sub> | <sub></sub> | <sub>2</sub> | <sub>2</sub> | <sub>2</sub> | <sub>2</sub>

A couple things to notice. There aren't enough Trackers, Rubbles or Zumas to use in any analysis. And Everest probably doesn't have enough data to compare, either, especially since she was a late addition to the pack.

And because the yearly totals of registrations varies so greatly, I need to normalize my data. This means that I take the count of each unique name and divide by the total dogs registered in that year. Noticing that Rocky is the most popular from my list, and that in 2016 there were 823 Rockies registered, from a total of 119,080 registrations, I want to normalize for the prevalence of each name to a fixed integer, so that I can compare years. In effect, how popular a certain name was in that year. The metric is then be `frequency of dog-name per 10000 dogs`.

### Closing the calculation

The math doesn't get too complicated, because the data doesn't require anything else. I'm going to use my normalized frequency metric to compare trends for Chase, Marshall, Rocky, Ryder, Rocky and Skye.

I've removed 2016 and 2017 now too, to try to more clearly show before and after. It's only Skye that shows any trend -- effectively doubling in popularity.

![paw patrol results]({attach}/images/paw_patrol_results.png)

## Step 4. Shutting it down

I can't believe I've spent this much time thinking about PAW Patrol. What I want to stress is that when you are working with data, for me it has been essential to 

1. Understand the subject matter. In this case, that means passively absorbing all things PAW Patrol.
 
2. Get dirty with the data. If you try to plug an algorithm on top of data, it's unlikely to give any meaningful results. Can you imagine creating a fancy data pipeline that spits out the 3 most popular dog names? `UNKNOWN`, `BELLA` and `NAME NOT PROVIDED`.

In case you haven't heard it already, here's their theme song. I've been singing it to myself as I write this, and I hope it gets stuck in your head, too.

<div class="youtube" align="center">
<iframe width="560" height="315" src="https://www.youtube.com/embed/1UdI_eoDPKQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>


# 🐶🦴 

### And remember--_Whenever there’s trouble, just yelp for help!_ 

---

---


### Footnotes

<sub>[1] For a less fun look at PAW Patrol's effect on society, take a look at this recent academic paper:</sub>

<sub>_[“Whenever there’s trouble, just yelp for help”: Crime, conservation, and corporatization in Paw Patrol](https://journals.sagepub.com/doi/abs/10.1177/1741659020903700)_</sub>

> <sub>I argue that the series suggests to audiences that we can and should rely on corporations and technological advancements to combat crime and conserve, with responsibilized individuals assisting in this endeavor.</sub>

> <sub>Ultimately, PAW Patrol echoes core tenets of neoliberalism and encourages complicity in a global capitalist system that (re)produces inequalities and causes environmental harms.</sub>