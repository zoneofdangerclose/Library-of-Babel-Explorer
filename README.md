# Library-of-Babel-Explorer
Fun data project for exploring API's, strings, and drawing order from chaos 

https://github.com/users/zoneofdangerclose/projects/1


Total number of words found: 4856

Longest sentence: ""

Most Coherent Paragraph: ""

Honorable Mentions:
<br><br>
The initial pass at this project was focused on brute force scanning of entries and comparing them to a dictonary of defined words. This led to some valuable things like:
<br>
1. Setting up the CLI tool for Library of Babel generation on the fly
1. Sharding the dictionary on the first letter of each work to reduce the O(nm) complexity by 26
1. Experience with the output and problem space

This solution proved to be too slow and it may be repurposed as a downstream filter check for promising entries. The second phase of this project is going to focus on using trigrams (three letter combinations commonly found at the begining or end of words) and using a scoring system to discover how much signal a page is producing before drilling deeper.

![Plot of scores from a random text example](<random density plot-1.png>)
<br>
![Plot of scores with a sentence in a random text example](<sentence density plot-1.png>)
<br><br>
Defining the optimal signal to noise threshold will need to take into account a few different cases:
1. Loose words
1. Sentence
1. Paragraph
1. Essay
<br>

However, before worrying about large scale order, the region of the problem space needs to be narrowed down. To find "hot" spots of valuable data I will use partical swarm optimization to sweep over different books to build a score density map. This rests on the assumption that the random generation algorithm will eventually start generating word like structures, which may be false.
<br><br>
![Partical Swam Optimization example](<PSO Example iteration_010-1.png>)
<br>
These density scores can eventually be used to allow words to coalesce together into sentence chains. Nearby words should "click" together like magnets with each word adding strength to the field like dense objects creating a gravitational field.
