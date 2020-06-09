
# T3020   Repo for ELEN3020

Name: Ivan Von Staden 1838664
Scott
Date: 7 June


# Description of code -- for question 1.1 and 1.2

The program `datamunger.py` is used to quality check data files. A
sample data file is given. The first row consists of headings which
the program ignores. The quality checks are

* The column TALL should be the sum of T1 through T8 inclusive
* For each of columns TALL and T1 through T7 inclusive (not T8),  the values increase monotonically. For example if in row 13, column T3 there's a value 49 (for example), then in row 14, column T3 the value should be 49 or greater.

Note, however, there is some missing data in some of the rows. The first few lines only contain values for TALL and only the latter half has values for OTHER.  If there are missing data for any row in columns TALL and T1 through T8 then that row should not be checked. However, we keep track of how many rows there are with missing data


### Errors

There are three deliberate errors, marked E1, E2 and E3. Finding other (non-deliberate and unknown to me)  errors will get a bonus -- clearly add below this line in your copy of the README what the errors are and how you fixed them.

E1 Fix

The error in E1 was that of an addition error, since the question said that it should be inclusive, in the calc_total function, The line:( for c in curr[2:9]:) had to be changed to (  for c in curr[1:9]: ) in order for the addition to work as intended

E2 Fix
After googling what montonomically meant, i found it meant that the current number would have to be smaller then the previous, thus in the check_monotonic(prev,curr) function, the line ( if curr[i] <=  prev[i]":" ) was incorrect as this would check if the current number was smaller or the same as the previous number. This was fixed by changing that line to: ( if curr[i] "<"  prev[i]: )


E3 Fix

The missing line count was wrong at 22 because it include the other column which was not specificed to be checked in the readme above, so i limited the search to stop at the 9th column so that it would not check the last column which fixed it and make it 15 lines which is correct. Below are the lines that were changed

for d in curr_str: ----> for d in curr_str[0:9]:


bonus error?
After fixing the 3 errors above, There was one error still left to do with the monotonically of the numbers. This was because the program was doing the check on T8 when it was supposed to be exclusive of column 8, Thus to fix this errror i went into the check_monotonic function and where the range was (for i in range(9) ): i changed it to be (for i in range(8):) this would exclude the 8th column from the check as it didnt need to be there.
