#!/usr/bin/env python
# coding: utf-8

# In[226]:


import cv2
import numpy


# In[227]:


arr = numpy.zeros((500,500,3))


# In[228]:


center_coordinates = (240, 200)
radius = 40
color = (255, 255, 255)
thickness = 3
image = cv2.circle(arr, center_coordinates, radius, color, thickness)


# In[229]:


center_coordinates = (240, 300)
radius = 60
color = (255, 255, 255)
thickness = 3
image = cv2.circle(arr, center_coordinates, radius, color, thickness)


# In[230]:


center_coordinates = (200, 160)
radius = 15
color = (255, 255, 255)
thickness = 3
image = cv2.circle(arr, center_coordinates, radius, color, thickness)


# In[231]:


center_coordinates = (280, 160)
radius = 15
color = (255, 255, 255)
thickness = 3
image = cv2.circle(arr, center_coordinates, radius, color, thickness)


# In[232]:


center_coordinates = (230, 190)
radius = 2
color = (255, 255, 255)
thickness = 10
image = cv2.circle(arr, center_coordinates, radius, color, thickness)


# In[233]:


center_coordinates = (250, 190)
radius = 2
color = (255, 255, 255)
thickness = 10
image = cv2.circle(arr, center_coordinates, radius, color, thickness)


# In[234]:


center_coordinates = (240, 205)
radius = 2
color = (255, 255, 255)
thickness = 8
image = cv2.circle(arr, center_coordinates, radius, color, thickness)


# In[235]:


cv2.imshow('smiley', arr)
cv2.waitKey()
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:




