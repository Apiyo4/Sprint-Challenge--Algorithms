#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(1) + O(n^3) + O(n^2) +O(1) which results to O(n^3)


b) 3O(1) + O(n) * O(log n)  which results to  O(n log n)


c) 2 O(1) + O(n) which results to O(n)

## Exercise II


Plan
In a n-storey building, the floors are ordered so we start from the zeroth floor to the nth-1 floor.
Therefore I'll be using binary search since it's the one with the least runtime O(log n)

Steps
  0. Have 2 variable that keeps count of the flloo when it breaks
  1. Get the middle of array gotten from spliting the number of floors, go to the floor and drop the egg
       -if egg breaks,
          add one to the count variable
          splice the array from beginning to the middle and then go back to step one
       -it it doesn't break ,
          splice the array from the middle to the end and then go back to step one
  2. Return the count variable

  Pseudocode
  1. have two var