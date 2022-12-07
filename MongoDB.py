from matplotlib import pyplot as plt
import numpy as np
# MongoDB 
# Queries 
# These are the parameters collected from the exection statistics of the queries without indexing, with complexity of O(n)
# docs_examined = Number of documents examined
docs_examined_On = []
# results_returned_On = Number of documents returned
results_returned_On = []
# Execution time of the query
exec_time_On = []
# Keys (index) examined returns are the number of keys exmined in each query 
keys_examined_On = []

# Case queries without indexing
# Query 1
'''
{"selector": { "Quantity": {"$eq": 6}}}
'''
# The numbers appended to the list are the results of the execution statistics 
docs_examined_On.append(100000)
results_returned_On.append(7407)
exec_time_On.append(70)
keys_examined_On.append(0)

# Query 2
'''
: {"selector": { "Quantity": {"$eq": 2}}}
'''
docs_examined_On.append(100000)
results_returned_On.append(15295)
exec_time_On.append(94)
keys_examined_On.append(0)

# Query 3
'''
{"selector": { "Quantity": {"$gt": 35}}}
'''
docs_examined_On.append(100000)
results_returned_On.append(22475)
exec_time_On.append(76)
keys_examined_On.append(0)

# Query 4 
'''
{"selector": { "Quantity": {"$lt": 35}}}
'''
docs_examined_On.append(100000)
results_returned_On.append(75971)
exec_time_On.append(72)
keys_examined_On.append(0)

#%%

# Case queries with indexing, queries complexities of O(1)
docs_examined_O1 = []
results_returned_O1 = []
exec_time_O1 = []

# Query 1
'''
{"selector": { "Quantity": {"$eq": 6}}}
'''
docs_examined_O1.append(7407)
results_returned_O1.append(7407)
exec_time_O1.append(39)
keys_examined_On.append(7407)

# Query 2
'''
: {"selector": { "Quantity": {"$eq": 2}}}
'''
docs_examined_O1.append(15295)
results_returned_O1.append(15295)
exec_time_O1.append(25)
keys_examined_On.append(15295)

#Warning create and index 

# Query 3
'''
{"selector": { "Quantity": {"$gt": 35}}}
'''
docs_examined_O1.append(22475)
results_returned_O1.append(22475)
exec_time_O1.append(44)
keys_examined_On.append(22475)


# Query 4 
'''
{"selector": { "Quantity": {"$lt": 35}}}
'''
docs_examined_O1.append(75971)
results_returned_O1.append(75971)
exec_time_O1.append(137)
keys_examined_On.append(75971)



#%%
# This case is complexity O(n)

plt.title("MongoDB execution statistics")
plt.xlabel('Results returned')
plt.ylabel('Execution time')
plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

plt.plot(results_returned_On, exec_time_On, 'r*')

plt.plot(results_returned_O1, exec_time_O1, 'b*')

plt.legend(["O(n)","O(1)"])
plt.show()



