#!/usr/bin/env python
# coding: utf-8

# # Programming Exercise 2: Constraint Satisfaction Problem

# <div class="alert alert-info">
#     <h3>Please read the following important information before starting with the programming exercise: </h3>
#     <p>In order to avoid problems with the relative file path we recommend to place the provided notebook and csp_programming_exercise.py file in the rootfolder of your <b>aima repository</b>.</p> 
#     <p>Do not use/install any additional packages, which are not provided in the requirements.txt of the  <b>aima repository</b>. </p>
#     <p>For modelling the constraint satisfaction problem you will have to define some variables. Do not change the names of variables that we provided you! Since we use these variables for an automatic evaluation, changing  variable names will result in failing the programming exercise. </p>
#     <p>Do not modify the example with the TWO + TWO = FOUR problem!</p>
#     <p>Do not modify the csp_programming_exercise.py!</p>
#     <p>After completing the exercise, download this jupyter notebook as *.py file (File &rarr; Download as 	&rarr; Python (.py)) </p>
#     <p>Before uploading this file together with your jupyter notebook to moodle, check if you can run <i>'python AI_Assignment2.py'</i> inside your anaconda environment in the root folder of your <b>aima repository</b>. If we are not able to run your submitted files in an environment with the packages provided by the requirements.txt of the <b>aima repository</b>, you will fail the programming exercise.</p>
#     
# </div>

# ## Initialization

# In[1]:


# Do not change this part.
from csp_programming_exercise import *
import sys, os
sys.path.append(os.path.realpath("aima"))


# ## Example for Solving a Constraint Satisfaction Problem

# In this exercise we are going to construct the Science Fair problem as a constraint satisfaction problem in Python using the csp library. The "TWO + TWO = FOUR" problem from the exercise (see Problem 3.4) will help us to understand how to model a constraint satisfaction problem with this library.
# 

# ### Constructing the Domains: TWO + TWO = FOUR

# We start with constructing the domains for our problem. As an example the domains for the TWO + TWO = FOUR- problem from the csp library are given. 

# In[2]:


# Do not change this part
# Here we form the domains for the variables: T, F, W, O, U, R, C1, C2 and C3
# Domains are formed using key-value pairs,
# where the key stands for the variable and the value is for the possible values
# set(range(1, 4)) is a short way of creating an array with numbers from 1 to 4
# set (range(1, 4)) == [1, 2, 3]
# Tip: Remember that you can construct arrays with any variable types

domains_TF = {'T': set(range(1, 10)),
           'F': set(range(1, 10)),
           'W': set(range(0, 10)),
           'O': set(range(0, 10)),
           'U': set(range(0, 10)),
           'R': set(range(0, 10)),
           'C1': set(range(0, 2)), 
           'C2': set(range(0, 2)), 
           'C3': set(range(0, 2))
}


# ### Constructing the Constraints: TWO + TWO = FOUR

# We continue with defining the constraints for our problem, the most important part of any constraint satisfaction problem. Let's take a look at the constraints for our "TWO + TWO = FOUR" problem to give you some insight about how to construct constraints with the csp library.

# In[3]:


# Do not change this part
# Here we define our constraints
# The constraint constructor of csp takes two arguments:
# 1. The variables that take part in the constraint
# 2. The constraint itself which is a function that takes the variables as arguments and returns true or false
# all_diff and eq are functions defined in csp 
# Like their name suggest all_diff returns true if every value is different
# and eq returns true if the two values are equal
# Tip: Take a look at the lambda operator in python https://www.w3schools.com/python/python_lambda.asp


constraint1_TF = Constraint(('T', 'F', 'W', 'O', 'U', 'R'), all_diff)
constraint2_TF = Constraint(('O', 'R', 'C1'), lambda o, r, c1: o + o == r + 10 * c1)
constraint3_TF = Constraint(('W', 'U', 'C1', 'C2'), lambda w, u, c1, c2: c1 + w + w == u + 10 * c2)
constraint4_TF = Constraint(('T', 'O', 'C2', 'C3'), lambda t, o, c2, c3: c2 + t + t == o + 10 * c3)
constraint5_TF = Constraint(('F', 'C3'), eq)


# ### Combine the constraints and set up the TWO + TWO = FOUR Problem

# In[4]:


# Do not change this part
# TWO + TWO = FOUR Problem
two_four_constraints = [constraint1_TF, constraint2_TF, constraint3_TF, constraint4_TF, constraint5_TF]
two_four = NaryCSP(domains_TF, two_four_constraints)


# ### Solve the TWO + TWO = FOUR Problem

# In[5]:


# Do not change this part
ac_search_solver(two_four)


# ## Programming Exercise Science Fair 

# ### Constructing the Domains: Science Fair

# In[6]:


# Define your domains here
projects = [         1         ,        2        ,            3           ,        4          ]
#names   = ["Solar Powered Car", "Potato Battery", "Baking Powder Volcano", "Our Solar System"]

students = [   1   ,     2   ,     3   ,     4    ,   5  ,   6   ,   7   ]
#names   = ["Bella", "Bethany", "Brian", "Brianna", "Ben", "Bill", "Bart"]

domains_SF = {}
for student in students:
    domains_SF[student] = projects


# ### Constructing the Constraints: Science Fair

# In[7]:


# Define your constraints here
def condition1(*all_s):
    """Everyone has a project: Every student is assigned to a project"""
    global projects
    
    for assignment in all_s:
        if assignment not in projects:
            return False
    return True

def condition2(*all_s):
    """No one presents alone: No project should be assigned to only one student"""
    global projects
    
    for project in projects:
        if (all_s.count(project) == 1):
            return False
    return True

def condition3(*all_s):
    """Each project must be presented at least by one student"""
    global projects
    
    for project in projects:
        if (all_s.count(project) == 0):
            return False
    return True

def condition4(*all_s):
    """Up to 4 students may work on the Solar Powered Car(1): 0 students possible"""
    if all_s.count(1) > 4:
        return False
    return True

def condition5(*all_s):
    """Up to 3 students may work on the Potato Battery(2): 0 students possible"""
    if all_s.count(2) > 3:
        return False
    return True
    
def condition6(*all_s):
    """At least 3 and at most 5 students may work on the Baking Powder Volcano(3): 0 students possible"""
    s_count = all_s.count(3)
    if (0 < s_count and s_count < 3) or s_count > 5:
        return False
    return True

def condition7(*all_s):
    """Our Solar System(4) is a project for 2 students: 0 students possible"""
    if all_s.count(4) != 0 and all_s.count(4) != 2:
        return False
    return True

def condition8(s1, s2):
    """Bart(7) presents together with Bethany(2) (i.e., other students could also present with them)"""
    if s1 != s2:
        return False
    return True
    
def condition9(s1, s2, s3):
    """Brian(3), Bill(6) and Ben(5) don’t want to present together because they don’t get along (i.e., any two of
them also don’t want to present together.)"""
    if s1 == s2 or s2 == s3 or s1 == s3:
        return False
    return True

def condition10(s1, s2):
    """Bill(6) and Brianna(4) don’t want to present the Baking Powder Volcano(3) because it’s boring"""
    if s1 == 3 or s2 == 3:
        return False
    return True

def condition11(s1, s2):
    """Bella(1) and Bill(6) present the Potato Battery(2) (i.e., other students could also present with them)"""
    if s1 != 2 or s2 != 2:
        return False
    return True

def condition12(s1, s2, s3):
    """Bella(1) presents with at least another girl beside herself: Bethany(2) or Brianna(4)"""
    if s1 == s2 or s1 == s3:
        return True
    return False

def condition13(*all_s):
    """No one presents Our Solar System(4)"""
    if all_s.count(4) != 0:
        return False
    return True

def condition14(s1, s2):
    """Brian(3) and Brianna(4) present together (i.e., other students could also present with them)"""
    if s1 != s2:
        return False
    return True

all_constraints = [
    Constraint(students, condition1),
    Constraint(students, condition2),
    Constraint(students, condition3),
    Constraint(students, condition4),
    Constraint(students, condition5),
    Constraint(students, condition6),
    Constraint(students, condition7),
    Constraint((2, 7), condition8),
    Constraint((3, 5, 6), condition9),
    Constraint((4, 6), condition10),
    Constraint((1, 6), condition11),
    Constraint((1, 2, 4), condition12),
    Constraint(students, condition13),
    Constraint((3, 4), condition14)
]


# ### Combine the constraints and set up the CSPs for the different problems

# <div class="alert alert-info">
#     <p>The variables csp_21, csp_22, .. are defined for setting up the CSPs for the corresponding problems. You have to use these variable names otherwise this will result in failing the programming exercise. For setting up the CSPs, you have to use the NaryCSP class (without any modifications) from the module csp_programming_exercise which was imported before. </p> 
# </div>

# In[8]:


# Construct the Science Fair Problems
def pick(consts, *indices):
    subset = []
    for i in indices:
        if hasattr(i, "__iter__"):
            for sub_i in i:
                subset.append(consts[sub_i-1])
        else:
            subset.append(consts[i-1])
    return subset

const_21 = pick(all_constraints, 1, 2, range(4, 13))               # { 1 – 2, 4 – 12 }
const_22 = pick(all_constraints, 1, range(3, 11), 12)              # { 1, 3 – 10, 12 }
const_23 = pick(all_constraints, 1, range(3, 8), range(10, 13))    # { 1, 3 – 7, 10 – 12 }
const_24 = pick(all_constraints, 1, 2, range(4, 8), range(10, 14)) # { 1 – 2, 4 – 7, 10 – 13}
const_25 = pick(all_constraints, 1, 2, range(4, 12), 13)           # { 1 – 2, 4 – 11, 13 }
const_26 = pick(all_constraints, 1, 2, range(4, 8), range(10, 15)) # { 1 – 2, 4 – 7, 10 – 14}

# Combine Constraints and set up the csp for Problem 2.1
csp_21 = NaryCSP(domains_SF, const_21)

# Combine Constraints and set up the csp for Problem 2.2 
csp_22 = NaryCSP(domains_SF, const_22)

# Combine Constraints and set up the csp for Problem 2.3
csp_23 = NaryCSP(domains_SF, const_23)

# Combine Constraints and set up the csp for Problem 2.4
csp_24 = NaryCSP(domains_SF, const_24)

# Combine Constraints and set up the csp for Problem 2.5
csp_25 = NaryCSP(domains_SF, const_25)

# Combine Constraints and set up the csp for Problem 2.6
csp_26 = NaryCSP(domains_SF, const_26)


# ### Solving the CSP

# <div class="alert alert-info">
#     <p>Do not change the following cell. If you can't execute the following cell, you may have renamed the variables defined by us.</p> 
# </div>

# In[9]:


print(ac_search_solver(csp_21))
print(ac_search_solver(csp_22))
print(ac_search_solver(csp_23))
print(ac_search_solver(csp_24))
print(ac_search_solver(csp_25))
print(ac_search_solver(csp_26))


# In[ ]:




