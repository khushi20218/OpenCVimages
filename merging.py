#!/usr/bin/env python
# coding: utf-8

# In[13]:


import cv2
import numpy


# In[14]:


photo1= cv2.imread('cat.jpg')
photo2= cv2.imread('dog.png')


# In[33]:


collagePhoto1= photo1[0:183, 0:200]
collagePhoto2= photo2[0:183, 0:200]


# In[34]:


cv2.imshow('photo1',collagePhoto1)
cv2.waitKey()
cv2.destroyAllWindows()


# In[35]:


cv2.imshow('photo1',collagePhoto2)
cv2.waitKey()
cv2.destroyAllWindows()


# In[36]:


collage= numpy.hstack((collagePhoto1,collagePhoto2))


# In[37]:


cv2.imshow('photo1',collage)
cv2.waitKey()
cv2.destroyAllWindows()


# In[ ]:




