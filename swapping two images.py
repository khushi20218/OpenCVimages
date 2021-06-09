#!/usr/bin/env python
# coding: utf-8

# In[14]:


import cv2


# In[35]:


cat = cv2.imread('cat.jpg')
dog = cv2.imread('dog.png')


# In[36]:


cv2.imshow('cat',cat)
cv2.waitKey()
cv2.destroyAllWindows()


# In[37]:


cv2.imshow('dog',dog)
cv2.waitKey()
cv2.destroyAllWindows()


# In[38]:


ccat = cat[40:145,  93:200].copy()


# In[39]:


cv2.imshow('ccat',ccat)
cv2.waitKey()
cv2.destroyAllWindows()


# In[40]:


cdog = dog[18:123,  89:196]


# In[41]:


cv2.imshow('cdog',cdog)
cv2.waitKey()
cv2.destroyAllWindows()


# In[42]:


#temp1=cat
cat[40:145,  93:200] = cdog


# In[ ]:





# In[44]:


dog[18:123,  89:196] = ccat


# In[43]:


cv2.imshow('photo1',cat)
cv2.waitKey()
cv2.destroyAllWindows()


# In[45]:


cv2.imshow('photo2',dog)
cv2.waitKey()
cv2.destroyAllWindows()


# In[ ]:




