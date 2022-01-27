# fill_portrait Package

## The Challenge
- How to find the optimized block size and grid size with the following conditions:
  - dimensions of the box holding the blocks
    - width
    - height
  - block aspect ratio
    - r = block_height / block_width
  - number of blocks
## sample result
```
{'count': 10000, 'height': 1200, 'r': 1.25, 'width': 450}
---- Scanning... ------
round	x	m	n	total_ratio
1 	 3.8088 	 118 	 252 	 33.58
2 	 5.6908 	 79 	 168 	 74.96
4 	 6.1612 	 73 	 155 	 87.87
5 	 6.3965 	 70 	 150 	 94.71
6 	 6.5141 	 69 	 147 	 98.23
10 	 6.5214 	 69 	 147 	 98.45
------------ Result Based on Converged m,n ----------------
10 	 6.5217 	 69 	 147 	 98.46
------------ Result Based on Converged x ----------------
10 	 6.5214 	 69 	 147 	 98.45
```