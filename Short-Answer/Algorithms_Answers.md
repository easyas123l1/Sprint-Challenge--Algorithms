#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) --> the first operation is n^3 but a is building up by n^2.  by dividing n^3 from n^2 we get O(n) 

b) O(n log n) --> the first loop is o(n) because its a pure iteration with no modifiers. The second loop (while loop) is log n because j grows at an  extremely fast rate with j *= 2 (growing to end the loop faster not slower).  This is what log n is.  When nested loops like this we multiple O(n) and O(log n) to get O(n log n)


c) O(n) --> this is similar to a for loop as we're iterating backwards by -1 til we hit the base case of 0. 

## Exercise II

The best approach for this would be a binary search.  A binary search would allow us to start from the middle floor of said building and drop the egg.  If the egg were to break we know to eliminate the top half of floors and go to the middle of the bottom half floors.  If the egg were not to break we would eliminate the bottom half of floors and go to the middle of the top half of floors.  We repeat this proccess which is known as a binary search.  We can do this because we know that all the floors of buildings are sorted.  Binary searchs have a time complexity of O(log n), this is because each search cuts the results down by half.  
