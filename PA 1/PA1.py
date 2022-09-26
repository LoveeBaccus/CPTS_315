# PA 1 Lovee Baccus

# Write a program using the A-priori algorithm to find products which are frequently browsed together. 
# Fix the support to s =100 (i.e., product pairs need to occur together at least 100 times to be 
# considered frequent) and find item sets of size 2 and 3.

# Read data from the file and load it into a data structure
# each line in the file is a basket, each item is seperated by whitespace
# items are represented as 8-character-long string IDs

# support threshold == 100, we are searching for subsets of size 2 and 3 (pairs and triples)
# use the A-priori algorithm