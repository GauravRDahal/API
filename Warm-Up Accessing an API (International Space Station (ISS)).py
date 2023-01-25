#!/usr/bin/env python
# coding: utf-8

# ### Using an API, let us find out who currently are on the International Space Station (ISS).
# ### The API at http://api.open-notify.org/astros.json gives us the information of astronauts currently on ISS in json format.
# ### You can read more about this API at http://open-notify.org/Open-Notify-API/People-In-Space/

# In[1]:


import requests # you need this module to make an API call
import pandas as pd


# In[4]:


api_url = "http://api.open-notify.org/astros.json" # this url gives use the astronaut data


# In[5]:


response = requests.get(api_url) # Call the API using the get method and store the
                                # output of the API call in a variable called response.


# In[7]:


if response.ok:             # if all is well() no errors, no network timeouts)
    data = response.json()  # store the result in json format in a variable called data
                            # the variable data is of type dictionary.


# In[8]:


print(data) # print the data just to check the output or for debugging


# In[20]:


data.keys()


# Print the number of astronauts currently on ISS.

# In[11]:


print(data.get("number"))


# Print the names of the astronauts currently on ISS.

# In[21]:


astronauts = data.get("people")
print("There are {} astronauts.".format(len(astronauts)))
print("And there names are:")
for astronaut in astronauts:
    print(astronaut.get("name"))

