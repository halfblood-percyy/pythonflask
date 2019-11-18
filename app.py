
# coding: utf-8

# In[4]:


from flask import Flask, render_template, request
from sklearn.externals import joblib
import pandas as pd
import numpy as np


# In[5]:


import pyodbc
server = 'percysqldbserver.database.windows.net'
database = 'percysqldb'
username = 'azureuser'
password = 'Qwerty@1234'
driver= '{ODBC Driver 17 for SQL Server}'


# In[6]:


app = Flask(__name__)


# In[7]:


@app.route("/")
def home():
    cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()
    cursor.execute("SELECT TOP 20 pc.Name as CategoryName, p.name as ProductName FROM [SalesLT].[ProductCategory] pc JOIN [SalesLT].[Product] p ON pc.productcategoryid = p.productcategoryid")
    row = cursor.fetchone()
    return(str(row[0]))


# In[8]:


if __name__ == "__main__":
    app.run(host='0.0.0.0')

