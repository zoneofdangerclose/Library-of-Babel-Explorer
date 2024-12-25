
# Language Distribution Research

## Rationale

The library of Babel generates random text and the purpose of this project is not to find the largest number of words,
it is to mine nuggets of "normal english human language" out of a random system. I came across the Zipf distribution some time
before this project and was struck that an infinitly complex thing like language could follow this mathmatical principle. (1) 

$$
f(r) \propto \frac{1}{(r+\beta)^{\alpha}}
$$

r = The frequency rank of the word (1st most popular, 2nd most, etc)<br>
α ≈ 1, scaling factor tied to Zipf's reseach (I need to dig into this more Zipf, 1936, 1949)<br>
β ≈ 2.7, A rank correction factor found to more closely fit the distribution (Mandelbrot, 1953,1962)<br>


The paper by Piantadosi applies the Zipf distribution to a large number of datasets, including works in different languages,
different kinds of words, and delimiting a text using "e" instead of a space. What is clear is that power distribution like
this is not infallible and that a R-squared value for a text can fit this line between 0.80 and 1.




References:
1. Steven T. Piantadosi, Zipf’s word frequency law in natural language: A critical review and future directions,
    Psychon Bull Rev. 2014 October ; 21(5): 1112–1130. doi:10.3758/s13423-014-0585-6.