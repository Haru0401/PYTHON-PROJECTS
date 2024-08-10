#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install openai


# In[4]:


import openai


# In[7]:



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

training_data = []

'''input '''
code = ['import numpy as np', 'import pandas as pd', 'import matplotlib.pyplot as plt']

for sent in code:
    loc_data = []
    for i in range(7, len(sent)-1):
        loc_data.append(sent[:i+1])
        loc_data.append(sent)
    training_data.append(loc_data)

for train_set in training_data:
    print('A:', train_set[0])
    print(':', train_set[1])


# ##  training_data[1]

# In[8]:




def get_response(final_prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=final_prompt,
        temperature=0.7,
        max_tokens=128,
        top_p=0.53,
        best_of=20,
        frequency_penalty=0.8,
        presence_penalty=0.98
    )
    return response['choices'][0]['text']


# In[9]:


import re

class Examples:
    def __init__(self):
        self.training_examples = []
        self.final_prompt_str = ""
        self.separator = " "  # Default separator
        self.in_sep = "A"
        self.out_sep = "B"

    def add(self, training_input, training_output):
        train_str = f"{self.in_sep}{training_input}{self.separator}{self.out_sep}{training_output}{self.separator}"
        self.training_examples.append(train_str)

    def add_prompt(self, prompt):
        self.final_prompt_str = self.get_examples() + self.in_sep + prompt + self.separator

    def get_final_prompt(self):
        return self.final_prompt_str

    def get_examples(self):
        example_str = ""
        for example in self.training_examples:
            example_str += example
        return (example_str)


# In[11]:


# Create an instance of the Examples class
try:
    train_examples = Examples()
except Exception as e:
    print(f"An error occurred: {e}")
    train_examples = Examples()

# Initialize count
count = 0

# Example data for demonstration purposes
training_data = [
    ["import numpy as np", "Import numpy as np"],
    ["import pandas as pd", "Import pandas as pd"],
    ["import matplotlib.pyplot as plt", "Import matplotlib.pyplot as plt"]
]

# Add training examples
for train_set in training_data:
    train_examples.add(train_set[0], train_set[1])
    count += 1
    # Uncomment the following lines if you want to break after a certain count
    # if count == 5:
    #     break

# Get and print all examples
print(train_examples.get_examples())


# In[ ]:




