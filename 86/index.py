# References

# Technically, vars are storing references to the computer memory locations where the values are stored.

spam = 42
cheese = spam
spam = 100
print(spam) # 100
print(cheese) # 42

# Integers are immutable values that don't change.
# changing the spam var is actually making it refer to a completely different value in memory
