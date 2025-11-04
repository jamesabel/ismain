Here are various benchmark results for different computers:

| Computer                 | Native Python (milliseconds) | `ismain` (milliseconds) |
|--------------------------|------------------------------|-------------------------|
| Intel Core i7            | 0.002                        | 50.825                  |
| Intel Core Ultra 9 285HX | 0.001                        | 12.509                  |

While the ratios between the "native" Python and ismain implementations are large, the absolute times are fairly small. 
This indicates that for many applications the performance of `ismain` may be acceptable.
