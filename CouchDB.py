from matplotlib import pyplot as plt
import numpy as np
# CouchDB 
# Queries 
# These are the parameters collected from the exection statistics of the queries without indexing, with complexity of O(n)
# docs_examined = Number of documents examined
docs_examined_On = []
# results_returned_On = Number of documents returned
results_returned_On = []
# Execution time of the query
exec_time_On = []

# Case queries without indexing
# Query 1
'''
{"selector": { "Quantity": {"$eq": 6}}}
'''
# The numbers appended to the list are the results of the execution statistics 
docs_examined_On.append(41)
results_returned_On.append(12)
exec_time_On.append(14)

# Query 2
'''
: {"selector": { "Quantity": {"$eq": 2}}}
'''
docs_examined_On.append(41)
results_returned_On.append(2)
exec_time_On.append(6)

# Warning receive create an index 

# Query 3
'''
{"selector": { "Quantity": {"$gt": 35}}}
'''
docs_examined_On.append(41)
results_returned_On.append(1)
exec_time_On.append(8)

# Warning create and index 

# Query 4 
'''
{"selector": { "Quantity": {"$lt": 35}}}
'''
docs_examined_On.append(41)
results_returned_On.append(39)
exec_time_On.append(12)

# Query 5
'''
{"selector": { "Quantity": {"$lt":   35}},"fields":"Invoce_No","Country"]}
'''
docs_examined_On.append(41)
results_returned_On.append(39)
exec_time_On.append(20)

# Query 6 
'''
{"selector": { "Quantity": {"$gt": 10}},"fields":"Invoce_No","Country"],"limit":5}
'''
docs_examined_On.append(0)
results_returned_On.append(5)
exec_time_On.append(28)

# Query 7
'''
{"selector": { "Quantity": {"$gt": 10}},"fields":"Invoce_No","Country"],"limit":30, "skip":4}
'''
docs_examined_On.append(41)
results_returned_On.append(11)
exec_time_On.append(4)

#%%

# Case queries with indexing, queries complexities of O(1)
docs_examined_O1 = []
results_returned_O1 = []
exec_time_O1 = []

# Query 1
'''
{"selector": { "Quantity": {"$eq": 6}}}
'''
docs_examined_O1.append(12)
results_returned_O1.append(12)
exec_time_O1.append(6)

# Query 2
'''
: {"selector": { "Quantity": {"$eq": 2}}}
'''
docs_examined_O1.append(2)
results_returned_O1.append(2)
exec_time_O1.append(5)

#Warning create and index 

# Query 3
'''
{"selector": { "Quantity": {"$gt": 35}}}
'''
docs_examined_O1.append(1)
results_returned_O1.append(1)
exec_time_O1.append(1)

# Query 4 
'''
{"selector": { "Quantity": {"$lt": 35}}}
'''
docs_examined_O1.append(39)
results_returned_O1.append(39)
exec_time_O1.append(11)

# Query 5
'''
{"selector": { "Quantity": {"$lt":   35}},"fields":"Invoce_No","Country"]}
'''
docs_examined_O1.append(39)
results_returned_O1.append(39)
exec_time_O1.append(12)

# Query 6 
'''
{"selector": { "Quantity": {"$gt": 10}},"fields":"Invoce_No","Country"],"limit":5}
'''
docs_examined_O1.append(5)
results_returned_O1.append(5)
exec_time_O1.append(4)

# Query 7
'''
{"selector": { "Quantity": {"$gt": 10}},"fields":"Invoce_No","Country"],"limit":30, "skip":4}
'''
docs_examined_O1.append(25)
results_returned_O1.append(11)
exec_time_O1.append(3)






#%%

plt.title("CouchDB execution statistics")
plt.xlabel('Results returned')
plt.ylabel('Execution time')
plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

plt.plot(results_returned_On, exec_time_On, 'r*')

plt.plot(results_returned_O1, exec_time_O1, 'b*')
#for xy in zip(results_returned_On, exec_time_On):
     #plt.annotate('(%.f, %.f)' % xy, xy=xy)

 #   for xy in zip(results_returned_O1, exec_time_O1):
   #plt.annotate('(%.f, %.f)' % xy, xy=xy)
plt.legend(["O(n)","O(1)"])
plt.show()

