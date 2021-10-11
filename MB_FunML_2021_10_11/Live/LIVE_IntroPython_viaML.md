# An Introduction to Python
### with a Machine Learning Context

---

### Aside: The Learning Approach

* think about a machine learning problem
    * quickly sketch some python code which will solve it
    * reflect on the python
    * exercise based on the code/solution we've developed
* may go by quickly
    * we're not teaching python!
    * we're just getting to basic levels of independent learning
* indepdenent exercise (c. 1hr)
    * review notebook
    * try code examples yourself
    * expand with exercise questions

<em><font color=#666> Q. questions are in gray. Answer by inserting a cell. </font></em>

---

## The Problem

* Problem Areas, Industries
    * Insurance
    * Health
    * Cooking
    * Security
    * Crime
    * Banking
    * Film, Media
    * Music
    * Logistics
* Crime
    * history of crimes
    * risk of violence:
        * probability of being violent
* Known Features $X$
    * Criminal Record
        * $X_0$ number of crimes
    * Personal Details
        * $X_1$ Area
        * $X_2$ Age
        * $X_3$ In Care System? 
* Unknown Target $y$
    * $y$ is whether you are a violent offender

## Python

### Datasets

* defining a variable `X`
    * a list `[, , , ]`
        * editable, expand, change
    * a tuple `(, , , )`
        * uneditable, fixed


```python
X = [
    (3, "London", 30, False),
    (4, "London", 20, True),
    (0, "Manchester", 18, True),
    (1, "Manchester", None, False), # could be a list [,,,,]
    (2, "Manchester", 50, False),
]
```

<em><font color=#666> Q. modify the definition of `X` to add a new row of data </font></em>

By making the rows uneditable ("immutable") the original dataset is always exactly how it was received. 

To change the dataset we derive *a new one*. 

##### Aside: `X` can be edited, eg., by appending a new element,


```python
X.append((10, "London", 21, True))
```


```python
X
```




    [(3, 'London', 30, False),
     (4, 'London', 20, True),
     (0, 'Manchester', 18, True),
     (1, 'Manchester', None, False),
     (2, 'Manchester', 50, False),
     (10, 'London', 21, True)]



<em><font color=#666> Q. append another row </font></em>

* If we can expand `X`, then we must likewise be able to expand `y`, 


```python
y = [
    True, 
    True, 
    False, 
    False, 
    False
]
```


```python
y.append(True)
```


```python
y
```




    [True, True, False, False, False, True]



<em><font color=#666> Q. `print()` X</em>

##### Checking Data Quality

`len()` is the number of elements in a data structure, 


```python
len(X)
```




    6




```python
len(y)
```




    6



The `==` symbol compares two values for equality,


```python
len(X) == len(y)
```




    True



<em><font color=#666> Q. Are `X` and `y` the same length? `.append` to one or the other and check. </em>

##### Aside: sum(y)


```python
y
```




    [True, True, False, False, False, True]



Why is `sum(y)` 3?


```python
sum(y)
```




    3



In python `True` is "a special version of `1`", and `False` is a "special version of `0`", 

What does `sum/len` of `y` tell you?


```python
sum(y) / len(y)
```




    0.5



"Empirical probability", the rate of `y` being `True` in **our dataset**. 

Rate of violent offenders in dataset, or "our probability" of seeing a violent offender. 

<em><font color=#666> Q. Define a list called `inspected` which is whether the crime has been investigated. Enter several `0` and `1`s in the list.</font></em>

<em><font color=#666> Q. What is the rate of inspected crimes? </font></em>

#### Checking the Elements of `X` and `y`

The `0` index is the first entry,


```python
X[0]
```




    (3, 'London', 30, False)




```python
y[0]
```




    True



<em><font color=#666> Q. Show the second elements of `X` and `y`</font></em>

In python list indexes are *positions*, and elments can be access "from the start" and "from the end", 


```python
X[0] # 0 = the start
```




    (3, 'London', 30, False)




```python
X[-1] # -1 = the end
```




    (10, 'London', 21, True)




```python
X[-2]
```




    (2, 'Manchester', 50, False)



<em><font color=#666> Q. Show the last element of `y` </font></em>

The fifth element along from the start, is also the second from the end,


```python
X[4] == X[-2]
```




    True



In `X`, each element has parts, 


```python
X[0]
```




    (3, 'London', 30, False)




```python
X[0][1]
```




    'London'




```python
X[0][-1]
```




    False



<em><font color=#666> Q. Show the number of crimes of the last person in `X` </font></em>

Consider `X[index][index]`,

* a variable name
    * `varibale[index]` -- FIND `index` IN `variable`
    * `...[index]` 
        * in lists and tuples `index` is a position
* `X[a][b]`
    * find `a` in `X`, in this element, find `b`


```python
X[0]
```




    (3, 'London', 30, False)




```python
X[0][3]
```




    False



##### Aside: This is just as,


```python
(3, 'London', 30, False)[3]
```




    False




```python
(3, 'London', 30, False)[-1]
```




    False



<em><font color=#666> Q. Change `False` to `True` in the tuples above. Why does the output change?  </font></em>

### Indexing Strings

Three quotes `"""` continue a piece text (ie., `string`) along several lines, 


```python
case_report = """The defendent was seen breaking &
entering through the window of the lower flat. 

-- Reporting Officer, Michael B. 
"""
```

`print()` will output a piece of text, including its newlines and formatting,


```python
print(case_report)
```

    The defendent was seen breaking &
    entering through the window of the lower flat. 
    
    -- Reporting Officer, Michael B. 
    



```python
case_report[4]
```




    'd'



Find the `0+4` (ie., 5th) position letter in the string, 


```python
"The defendent was seen breaking &"[4]
```




    'd'




```python
"space "[-1]
```




    ' '



<em><font color=#666> Q. Define another case report using `"""` strings. Show the 100th character.  </font></em>

### Selecting Multiple Elements: Slicing

In python you can select multiple elements at once, ie., taking a *slice*, 


```python
X
```




    [(3, 'London', 30, False),
     (4, 'London', 20, True),
     (0, 'Manchester', 18, True),
     (1, 'Manchester', None, False),
     (2, 'Manchester', 50, False),
     (10, 'London', 21, True)]




```python
X[0]
```




    (3, 'London', 30, False)



The first two, 


```python
X[0:2]
```




    [(3, 'London', 30, False), (4, 'London', 20, True)]



<em><font color=#666> Q. Show the first two entires in `y`.  </font></em>

We include the element at the `start_index`, and keep including until (but not) the `end_index`, 

`X[ start_index : end_index ]`


```python
X[1:3]
```




    [(4, 'London', 20, True), (0, 'Manchester', 18, True)]



<em><font color=#666> Q. In your case report above, show the characters from the first letter to the 10th letter.  </font></em>

And we can use reversed indexes,


```python
X
```




    [(3, 'London', 30, False),
     (4, 'London', 20, True),
     (0, 'Manchester', 18, True),
     (1, 'Manchester', None, False),
     (2, 'Manchester', 50, False),
     (10, 'London', 21, True)]



Third from the end, `-3`, *until* one from the end `-1`, 


```python
X[-3:-1]
```




    [(1, 'Manchester', None, False), (2, 'Manchester', 50, False)]



If you leave off the `start_index`, python assumes `0`. 

If you leave off the `end_index`, python assumes `len(X)`, ie. until the end.


```python
X[:2]
```




    [(3, 'London', 30, False), (4, 'London', 20, True)]



<em><font color=#666> Q. Show the first two entires in `y` without using `0` as the starting index.</font></em>


```python
X[0:2]
```




    [(3, 'London', 30, False), (4, 'London', 20, True)]




```python
X[-2:]
```




    [(2, 'Manchester', 50, False), (10, 'London', 21, True)]



<em><font color=#666> Q. Show the last two entires in `y` likewise.  </font></em>

Aside, to write this explicitly, `len(X)` is the last index in `X`, 


```python
len(X)
```




    6




```python
X[-2:len(X)]
```




    [(2, 'Manchester', 50, False), (10, 'London', 21, True)]



Leaving off both means "all", 


```python
X[:]
```




    [(3, 'London', 30, False),
     (4, 'London', 20, True),
     (0, 'Manchester', 18, True),
     (1, 'Manchester', None, False),
     (2, 'Manchester', 50, False),
     (10, 'London', 21, True)]



This is the same as `X`,


```python
X
```




    [(3, 'London', 30, False),
     (4, 'London', 20, True),
     (0, 'Manchester', 18, True),
     (1, 'Manchester', None, False),
     (2, 'Manchester', 50, False),
     (10, 'London', 21, True)]



<em><font color=#666> Q. why does `y == y[:]` ? </font></em>

### Process the Dataset


```python
X
```




    [(3, 'London', 30, False),
     (4, 'London', 20, True),
     (0, 'Manchester', 18, True),
     (1, 'Manchester', None, False),
     (2, 'Manchester', 50, False),
     (10, 'London', 21, True)]



We could manually repeat `print(row)` for every element in `X`,


```python
row = X[0]
print(row)

row = X[1]
print(row)

row = X[2]
print(row)

row = X[3]
print(row)

# and so on...
```

    (3, 'London', 30, False)
    (4, 'London', 20, True)
    (0, 'Manchester', 18, True)
    (1, 'Manchester', None, False)


Or, this loop will assign `row` for us *to be* each element in `X` from the start until the end, 


```python
for row in X: 
    print(row)
```

    (3, 'London', 30, False)
    (4, 'London', 20, True)
    (0, 'Manchester', 18, True)
    (1, 'Manchester', None, False)
    (2, 'Manchester', 50, False)
    (10, 'London', 21, True)


<em><font color=#666> Q. modify the definition of loop to print the first entry in each row, ie., the number of crimes. </font></em>

And then repeat the code which is *indented*.

### Looping to inspect the data, 

A  data quality inspection report, 


```python
for row in X: 
    print("Num Crimes\t", row[0])
    print("In care?\t",  row[-1])
    print()
```

    Num Crimes	 3
    In care?	 False
    
    Num Crimes	 4
    In care?	 True
    
    Num Crimes	 0
    In care?	 True
    
    Num Crimes	 1
    In care?	 False
    
    Num Crimes	 2
    In care?	 False
    
    Num Crimes	 10
    In care?	 True
    


<em><font color=#666> Q. complete the report, show all elements of each row.  </font></em>

## Stretch Questions

<p><em><font color=#666>1. Create a new notebook .</font></em></p>
<p><em><font color=#666>2. Choose a different problem domain.</font></em></p>
<p><em><font color=#666>3. Consider a dataset of features $X$, targets $y$ .</font></em></p>
<p><em><font color=#666>4. Reporduce this analysis for your own problem.</font></em></p>


<p><em><font color=#666> Eg. Health, Sleep Quality, X = ...(HR, BP, Hours), y = [GOOD, BAD, OK]... .</font></em></p>

## Advice for Novices

* Create a new notebook
* **TYPE OUT!**
    * the code examples given
    * (you need to understand the syntax, ie., to type it!)
* Gradually modify these examples & experiment to see what they do
* Do this for all the examples
* Go back and do the questions

# Part 2: Complex Looping & Conditions

## Preview of the Solution


```python
X = [
    (3, "London", 30, False),
    (4, "London", 20, True),
    (0, "Manchester", 18, True),
    (1, "Manchester", 20, False), 
    (2, "Manchester", 50, False),
    (10, 'London', 21, True)
]
```


```python
violents = {'crimes': [], 'locations': [], 'age': [], 'in_care': []}

for features, target in zip(X, y):
    if target:
        violents['crimes'].append(features[0])
        violents['locations'].append(features[1])
        violents['age'].append(features[2])
        violents['in_care'].append(features[3])

```


```python
from statistics import mode, mean 

factors = {
    'crime': mean(violents['crimes']),
    'location': mode(violents['locations']),
    'age': mean(violents['age']),
    'in_care': mean(violents['in_care']),
}

factors
```




    {'crime': 5.666666666666667,
     'location': 'London',
     'age': 23.666666666666668,
     'in_care': 0.6666666666666666}




```python
new_X = (2, "London", 27, False)

score = (
    new_X[0] * factors['crime'] + 
    new_X[2] * factors['age'] + 
    new_X[3] * factors['in_care'] + 
    100 * int(new_X[1] == factors['location']) 
)
```


```python
score
```




    750.3333333333334




```python
if score >= 1000:
    print("VIOLENT")
else:
    print("NON-VIOLENT")
```

    NON-VIOLENT


---

## Appendix


```python
isinstance(False, int)
```




    True




```python

```
