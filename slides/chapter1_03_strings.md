---
type: slides
---

# Making use of strings

Notes: Strings are another cool built-in data type. It's very likely that some of the variables you will be working with in a future will be in a `str` format, so it's important to understand how to deal with them.

---

# What are strings?

In a fancy way we can say that strings are **immutable** sequences of Unicode code points. In a simple way we can say that strings are the sequences of "characters", that cannot be changed.

```python
x = "Neuroscience Rocks!"
# print the length of the string (how many characters are in the string)
print(len(x))
```

```out
19
```

```python
print("You " + "can " + "also " + "add " + "strings!")
print("Or even multiply!"*3)
```

```out
You can also add strings!
Or even multiply!Or even multiply!Or even multiply!
```

Notes: You might have seen codes like this:

```python
x = "Hello" # single brackets
```
```python
x = 'Hello' # double brackets
```

What are the differences? There is absolutely no difference which type of brackets you are going to use, as long you are consistent within one string (for example, `"hello'` would raise an Error).

---

# Slicing

Python allows to get slices from the string by calling

```python
string[start:end:step]
```

* `start` - index where you want to start the slicing (included)
* `end` - index where you want to end the slicing (not included)
* `step` - step of the slice (for example, every second value); default is 1

```python
s = "Neuroscience Rocks!"
print(s[5:12]) # example 1
print(s[5]) # example 2
print(s[:4]) # example 3
print(s[::2]) # example 4
print(s[::-1]) # example 5
```

```out
science
s
Neur
Nuocec ok!
!skcoR ecneicsorueN
```
Notes: You can take a slice from the string by calling its index(es) in square brackets. It's important to remember, that indexes in Python start with 0 (letter `N` in a string `Neuroscience` stands on a 0th index, not the 1st one).

In the first example we are taking all the characters from 5th index to 11th included. We can drop the `:step` part if we want to take all the values.

In the second example we provide only starting index. In such case we return just one character, that stands on a 5th index.

In the third example we drop starting index, but provided end index. That means that Python takes the values from the beginning till 3th index included.

In the fourth example we drop both starting and end index, meaning that we want to take elements from the beginning till the end (all values basically). However, step is set to 2, meaning that we take every second value.

In the last example we are taking again all the values. Step of `-1` returns reversed string.

---

# Check occurrence

```python
mRNA = "GUAUGCACGUGACUUUCCUCAUGAGCUGAU"
leucine_codon = "CUC"
leucine_codon in mRNA
```

```out
True
```

```python
arginine_codon = "CGC"
arginine_codon not in mRNA
```

```out
True
```

**BUT**:

```python
leucine_codon = "cuc"
leucine_codon in mRNA
```

```out
False
```

Notes: Another useful trick is to check whether a string hold some other stings using `in` operator. Note, that strings are case sensitive so `"CUC"` and `"cuc"` are two different strings.

---

# Strings' methods

```python
s = "Neuroscience Rocks!"

# basic string methods (does not modify the original string)
s.lower() # returns 'neuroscience rocks!'
s.upper() # returns 'NEUROSCIENCE ROCKS!'
s.startswith('brain') # returns False
s.endswith('!') # returns True
s.isdigit() # returns False (returns True if every character in the string is a digit)
s.find('science') # returns index of first occurrence (5), but doesn't support regex
s.find('Psychology') # returns -1 since not found
s.replace('Neuro','Brain') # replaces all instances of 'Neuro' with 'Brain'

print(s)
```

```out
Neuroscience Rocks!
```

Notes:

Note that some (or even most) of the methods, don't change the original object. In our example we applied multiple methods on the string `s`, but at the end it was still the same. If we want to save the modification after method application we need to assign it to a variable.

```python
s = "Neuroscience Rocks!"
# rewrite the variable
s = s.upper()
```

---

# Let's code!