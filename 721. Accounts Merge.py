# Jun 02 2020
# Union Find

from typing import List
class Solution:
    def find(self,parent_array,i):
        if parent_array[i] == i:
            return i
        else:
            return self.find(parent_array,parent_array[i])
    
    def union(self,parent_array,i,j):
        
        x = self.find(parent_array,i)
        y = self.find(parent_array,j)
        # if x != y :
        parent_array[x] = y


    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = []
        for i in range(len(accounts)):
            parent.append(i)
        # email_to_name = dict()
        email_to_i = dict()
        for account_i in range(len(accounts)):
            for email in accounts[account_i][1:]:
                if email not in email_to_i:
                    email_to_i[email] = account_i
                else:
                    self.union(parent,account_i,email_to_i[email])
                    email_to_i[email] = self.find(parent,i)
        
#         for i in range(len(accounts)):
#             for email in accounts[i][1:]:
#                 email_to_i[email] = self.find(parent,i)
        
        result = dict()
        for i in range(len(accounts)):
            for email in accounts[i][1:]:
                if parent[i] not in result:
                    result[parent[i]] = set()                
                result[parent[i]].add(email)
        print(parent)
        
        return [[accounts[k][0]] + sorted(result[k]) for k in result.keys()]
        
        