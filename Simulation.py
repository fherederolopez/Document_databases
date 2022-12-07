from matplotlib import pyplot as plt
import numpy as np

### First simulation, comparative between MongoDB and CouchDB

Couch_docs_examined_O1 = []
Couch_results_returned_O1 = []
Couch_exec_time_O1 = []

# Q1
'''
Q2: {"selector": { "Quantity": {"$eq": 6}}}
'''
Couch_docs_examined_O1.append(12)
Couch_results_returned_O1.append(12)
Couch_exec_time_O1.append(12)

#Q2
'''
Q2: {"selector": { "Quantity": {"$eq": 2}}}
'''
Couch_docs_examined_O1.append(2)
Couch_results_returned_O1.append(2)
Couch_exec_time_O1.append(6)


#Q3
'''
Q3: {"selector": { "Quantity": {"$gt": 35}}}
'''
Couch_docs_examined_O1.append(1)
Couch_results_returned_O1.append(1)
Couch_exec_time_O1.append(1)


#Q4
'''
Q4: {"selector": { "Quantity": {"$lt": 35}}}
'''
Couch_docs_examined_O1.append(39)
Couch_results_returned_O1.append(39)
Couch_exec_time_O1.append(24)

#%%

Mongo_docs_examined_O1 = []
Mongo_results_returned_O1 = []
Mongo_exec_time_O1 = []

# Q1
'''
Q2: {"selector": { "Quantity": {"$eq": 6}}}
'''
Mongo_docs_examined_O1.append(12)
Mongo_results_returned_O1.append(12)
Mongo_exec_time_O1.append(0)

#Q2
'''
Q2: {"selector": { "Quantity": {"$eq": 2}}}
'''
Mongo_docs_examined_O1.append(2)
Mongo_results_returned_O1.append(2)
Mongo_exec_time_O1.append(0)

#Warning create and index 

#Q3
'''
Q3: {"selector": { "Quantity": {"$gt": 35}}}
'''
Mongo_docs_examined_O1.append(1)
Mongo_results_returned_O1.append(1)
Mongo_exec_time_O1.append(0)

#Q4
'''
Q4: {"selector": { "Quantity": {"$lt": 35}}}
'''
Mongo_docs_examined_O1.append(29)
Mongo_results_returned_O1.append(29)
Mongo_exec_time_O1.append(0)


#%%
plt.title("CouchDB and MongoDB")
plt.xlabel('Results returned')
plt.ylabel('Execution time')
plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

plt.plot(Mongo_results_returned_O1, Couch_exec_time_O1, 'r*')

plt.plot(Mongo_results_returned_O1, Mongo_exec_time_O1, 'b*')
#for xy in zip(results_returned_On, exec_time_On):
     #plt.annotate('(%.f, %.f)' % xy, xy=xy)

 #   for xy in zip(results_returned_O1, exec_time_O1):
   #plt.annotate('(%.f, %.f)' % xy, xy=xy)
plt.legend(["CouchDB","MongoDB"])
plt.show()







#%%

### This is the information of execution statistics provided by CosmosDB in the queries

Cosmos_docs_examined_O1 = []
Cosmos_results_returned_O1 = []
Cosmos_exec_time_O1 = []
Cosmos_index_lookup_time_O1 = []
Cosmos_docload_time_O1 = []
Cosmos_queryengine_exec_time_O1 = []
Cosmos_System_function_exec_O1 = []
Cosmos_User_defined_func_exec_O1 = []

# Q1
'''
Q2: {"selector": { "Quantity": {"$eq": 6}}}
'''
Cosmos_docs_examined_O1.append(12)
Cosmos_results_returned_O1.append(12)
Cosmos_exec_time_O1.append(0)
Cosmos_index_lookup_time_O1.append(0.18)
Cosmos_docload_time_O1.append(0.06)
Cosmos_queryengine_exec_time_O1.append(0.07)
#Q2
'''
Q2: {"selector": { "Quantity": {"$eq": 2}}}
'''
Cosmos_docs_examined_O1.append(2)
Cosmos_results_returned_O1.append(2)
Cosmos_exec_time_O1.append(0)
Cosmos_index_lookup_time_O1.append(0.07)
Cosmos_docload_time_O1.append(0.02)
Cosmos_queryengine_exec_time_O1.append(0.03)
#Warning create and index 

#Q3
'''
Q3: {"selector": { "Quantity": {"$gt": 35}}}
'''
Cosmos_docs_examined_O1.append(1)
Cosmos_results_returned_O1.append(1)
Cosmos_exec_time_O1.append(0)
Cosmos_index_lookup_time_O1.append(0.06)
Cosmos_docload_time_O1.append(0.01)
Cosmos_queryengine_exec_time_O1.append(0.04)
#Q4
'''
Q4: {"selector": { "Quantity": {"$lt": 35}}}
'''
Cosmos_docs_examined_O1.append(29)
Cosmos_results_returned_O1.append(29)
Cosmos_exec_time_O1.append(0)
Cosmos_index_lookup_time_O1.append(0.07)
Cosmos_docload_time_O1.append(0.13)
Cosmos_queryengine_exec_time_O1.append(0.15)


#%%
plt.title("Execution statistics")
plt.xlabel('Results returned')
plt.ylabel('Execution time (ms)')
plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

plt.plot(Cosmos_results_returned_O1, Cosmos_index_lookup_time_O1, 'r*')

plt.plot(Cosmos_results_returned_O1, Cosmos_docload_time_O1, 'b*')

plt.plot(Cosmos_results_returned_O1, Cosmos_queryengine_exec_time_O1, 'g*')
#for xy in zip(results_returned_On, exec_time_On):
     #plt.annotate('(%.f, %.f)' % xy, xy=xy)

 #   for xy in zip(results_returned_O1, exec_time_O1):
   #plt.annotate('(%.f, %.f)' % xy, xy=xy)
plt.legend(["CouchDB","MongoDB","CosmosDB"])
plt.show()
#%%

