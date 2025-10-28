# A transaction is possibly invalid if:

# the amount exceeds $1000, or;
# if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.
# You are given an array of strings transaction where transactions[i] consists of comma-separated values representing the name, time (in minutes), amount, and city of the transaction.

# Return a list of transactions that are possibly invalid. You may return the answer in any order.

 

# Example 1:

# Input: transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
# Output: ["alice,20,800,mtv","alice,50,100,beijing"]
# Explanation: The first transaction is invalid because the second transaction occurs within a difference of 60 minutes, have the same name and is in a different city. Similarly the second one is invalid too.
# Example 2:

# Input: transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
# Output: ["alice,50,1200,mtv"]
# Example 3:

# Input: transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
# Output: ["bob,50,1200,mtv"]


"""
Transaction is invalid if:
- amount > $1000
- a transaction from same name occurs within last 60mins from another city

cases:
if amount > $1000 -> invalid
else
    transactions with same name with different city <= 60 mins -> invalid
    transactions with same name with different city > 60 mins -> valid
    transactions with same name with same city -> valid
    transactions with different name with same/diff city -> valid
}

plan:
- parse this transaction into name, time (in minutes), amount, and city
- Group this parsed transaction by name in dict (hashmap) {name: [record1, record2]} where records will always be sorted
- While building this dict, we can check our cases and add the invalid transactions to our final list (invalid_transactions)
- return the final list invalid_transactions
"""

def invalidTransactions(transactions: list[str]) -> list[str]:

    invalid_transactions = set()
    transactions_by_name = dict()

    for idx, transaction in enumerate(transactions): # O(n)
        name, time, amount, city = transaction.split(",") #parsing the transaction details

        # building the transactions_by_name dict
        if name in transactions_by_name:
            transactions_by_name[name].append((int(time), city, idx))
        else:
            transactions_by_name[name] = [(int(time), city, idx)]

        # checking amount constraint
        if int(amount) > 1000:
            invalid_transactions.add(idx)

        for time_record, city_record, idx_by_name in transactions_by_name[name]: #O(m)
            # checking transactions with same name with different city <= 60 mins
            if city != city_record and abs(int(time) - time_record) <= 60:
                invalid_transactions.add(idx_by_name)
                invalid_transactions.add(idx)
            
    res = []
    for i in invalid_transactions:
        res.append(transactions[i])
    return res


"""
TC: O(n * m) where n -> size of transactions and m -> records under each name
~ O(n^2)
SC: O(n + k) for storing the dict and set
"""


