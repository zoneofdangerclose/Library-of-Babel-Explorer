# Library-of-Babel-Explorer
Fun data project for exploring API's, strings, and drawing order from chaos 

https://github.com/users/zoneofdangerclose/projects/1

The filtering is agressive, the point is not to find ever word, but to find clusters of probable words to locate larger messages.

Total number of words found: 4856

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
Going through 400 volumes show that pages with a single word and pages with two words may have a different mean percentage of words that pass filter.<br>
![LoB histogram 20240729](https://github.com/user-attachments/assets/b66cebd5-e001-4736-9caa-7891990d4080)
<br><br>
A t-test of the two different populations has a p-value of 2.69E-4, indicating that they are different and there is likely a possiblity of filtering out entire pages just based on the percentage of words of a certain length that appear and the need to check if those words are defined is unneccisary, saving O(nm) time due to not needing to compare the word to the dictionary. It will be interesting to see if this trend follows the Zipf distrubtion as pages with >2 defined words are found. The strick filter removes the most popular short words like "of", "is" and, "the", so a recursive look at the page with a looser filter may be required once a critcal threshold of defined words are found.
<br><br>
The mean and standard deviation for the total number of words that pass filter for the two groups (total pop. 4856) breaks down like this:<br>

|Group|Mean|stdev|
|-----|----|-----|
|Single words|13.9%|3.0%|
|Two words|15.2%|3.1%|

<br>
The difference in mean between a single word getting defined and two words getting defined is 1.3%, with comparable standard deviations. Assuming this
relationship is linear, then a page with three words will have a mean of 16.5% and a page with ten words will be around 26.9%. <br>
