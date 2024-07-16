# Library-of-Babel-Explorer
Fun data project for exploring API's, strings, and drawing order from chaos 

https://github.com/users/zoneofdangerclose/projects/1

The filtering is agressive, the point is not to find ever word, but to find clusters of probable words to locate larger messages.

Total number of words found: 1294

Longest sentence: ""

Most Coherent Paragraph: ""

Honorable Mentions:
<br><br>
The percent of words that pass filtering has a normal distribution. This is a truely random system so it would be expected to have a normal distribution
and that means we can easily perform some statistical analysis and find outliers. Maybe it is worth screening out any pages that aren't outliers. 
<br>
![Historgram of Undefined Words that passed filter](https://github.com/zoneofdangerclose/Library-of-Babel-Explorer/assets/148597567/90c9c289-661d-421e-bf46-d65b85c56493)
<br><br>
From the first book, there does not appear to be a correlation between the number of words that pass filter and the number of words that ultimately have definitions. However, I also have not encountered a page with more than one word.
<br><br>
Going through the first 100 volumes show that pages with a single word and pages with multiple words may have a different mean percentage of words that pass filter.
![Pass_Filter_Comparison](https://github.com/user-attachments/assets/860bdc27-f204-4fe6-8616-52426cb0a320)
<br><br>
A t-test of the two different populations has a p-value of 0.085, indicating that they are different and there is likely a possiblity of filtering out entire pages just based on the percentage of words of a certain length that appear and the need to check if those words are defined is unneccisary, saving O(nm) time due to not needing to compare the word to the dictionary. It will be interesting to see if this trend follows the Zipf distrubtion as pages with >2 defined words are found. The strick filter removes the most popular short words like "of", "is" and, "the", so a recursive look at the page with a looser filter may be required once a critcal threshold of defined words are found.
