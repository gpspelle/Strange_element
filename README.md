# Strange Element

This code was built to find a strange element in a 4 and 3 size sequences.
Example: which is the strange element in [88, 120, 150, 200] and [90, 119, 210]? 

Ans: 150. 

## Code 

First I thought in a really sofisticated graph approach to this problem and
tried to find the strange element by removing edges, where each edge contains
the absolute value between from an element of each sequence. But this failed in
case t2.in.

The second approach is to find the element that if removed causes the sum of the
difference of the elements in order to be the smallest, it seems to give an
better result.


