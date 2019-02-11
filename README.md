# InsightChanllenge

## Summary and Instructions

This code counts the frequency of a drug being presribed and the total cost.

To run the code, execute run.sh as an executable. The output of the programs can be found in the output folder as a text file labeled "total_drug_cost.txt".

## Libraries Required
My code uses sys, collection, re, csv libraries

## Inputs
My code takes one text input:

itcont.txt

The code uses five fields from the itcont.txt file, with the following considerations:

id: cannot be null
prescriber_last_name: can be null
prescriber_first_name: can be null
drug_name: cannot be null
drug_cost: must be numeric

## Approach

My code uses the following approach:

* Process the input file one line at a time to aviod the memory required to read an entire file especially when input size is larger than system RAM.

* Filter out records that do not satisfy requirement above.

* Use dictionaries to store number of prescriber and total cost of drug. Store total_drug_cost as an ordered dictionary sorted by cost in descending order, then output to text file. number of prescriber can be looked up in O(1) time complexity which makes the algorithm efficient even with large amount of records. This program runs in O(n) time complexity where n is number of records.
