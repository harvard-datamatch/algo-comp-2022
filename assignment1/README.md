# Assignment 1: Scoring

In this assignment, you will implement a lightweight scoring function of your choice. You are free to design your scoring function however you like, but may find the design discussions we've had during our comp meetings helpful. 

This assignment will be implemented in **Python** and most of your code will be in the `main.py` file, where you will implement the `compute_score` function.

## Setup and Logistics
This assignment is due on **Thursday, October 21st at 11:59 PM EST**. We recommend forking this repository and then sending either one of us (Jeremy or Leonard) the link when you're ready. When you fork, make sure to set this repository as the upstream repository so you can pull any changes we make. **We will not be making any changes to `compute_score`** so if you only write code within that function, you can pull without worrying about encountering merge conflicts.

**Don't worry** if you are unfamiliar with using Git or Python. We will be providing docs on both that'll give you what you need to get started very soon (Jeremy needs to finish CS 165 and Stat 110 first)! In the meantime, we recommend checking out some articles on Google.

## Code Layout
To make this more straightforward, we have provided a `User` class with a few attributes that you would find in Datamatch's main scoring algorithm:
```python
class User:
    def __init__(self, name, gender, preferences, grad_year, responses):
        self.name = name # str
        self.gender = gender # str
        self.preferences = preferences # List[str] (e.g. ['M'])
        self.grad_year = grad_year # int (e.g. 2022, 2023, 2024, 2025)
        self.responses = responses List[int] (e.g. [0, 1, 2, 3, 1])
```
Note that for  `responses`, each index represents a question and the value stored at that index refers to the answer choice for that question (so in our above case, that person picked `2` for question `2`).

Your task for this assignment will be to implement `compute_score`. `compute_score` takes in two `User` objects and outputs a float denoting their compatibility. One thing to consider is that we want all compatibility scores to be **normalized** across some defined scale (usually this is from `0` to `1`). This helps us better understand the relative differences between two scores (e.g. `6` vs. `7` normalized on `0-10` means something different than `6` vs. `7` normalized on `0-20`.

## Running Your Code
```python3 main.py```

## Collaboration
Collaboration on high-level design is allowed and actually **highly encouraged** as this mimics the sorts of discussions we'll be having when designing Datamatch's main algorithm. We're going to spend our open design discussion time during the October 12th meeting talking about scoring again so you can share the choices and considerations you made and hear other compers did.

As for code sharing, we certainly won't police you if your code looks suspiciously similar to someone else's but still encourage to write your own code as it'll better prepare you for your projects down the line.

## Other
If you have any questions, don't hesitate to directly reach out to **Jeremy Hsu** or **Leonard Tang** on Slack!
