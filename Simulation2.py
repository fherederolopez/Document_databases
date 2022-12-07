from matplotlib import pyplot as plt
import numpy as np

### This script correspond to the second simulation
Mdocs_examined = []
Mresults_returned = []
Mexec_time = []
Mkeys_examined = []

Cdocs_examined = []
Cresults_returned = []
Cexec_time = []
Ckeys_examined = []

# Q1

Mexec_time.append(89)
Mresults_returned.append(3443)
Cexec_time.append(476)
Cresults_returned.append(3443)

# Q2
Mresults_returned.append(7749)
Mexec_time.append(37)

Cexec_time.append(358)

# Q3

Mexec_time.append(36)

Cexec_time.append(321)

# Q4

Mexec_time.append(62)

Cexec_time.append(620)




#%%
query = ["Q1","Q2","Q3","Q4"]

X_axis = np.arange(len(query))

plt.bar(X_axis-0.2,Mexec_time,0.4, label = 'MongoDB')
plt.bar(X_axis+0.2,Cexec_time,0.4, label = 'CosmosDB')

plt.xticks(X_axis, query)
plt.xlabel("Queries")
plt.ylabel("Execution time")
plt.title("CosmosDB vs MongoDB execution statistics")
plt.xlabel("Queries")
plt.legend(["MongoDB","CosmosDB"])
plt.show()








