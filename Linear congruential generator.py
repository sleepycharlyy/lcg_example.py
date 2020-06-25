# imports
import time
import math

# parameters
seed = int(round(time.time() * 1000))
multiplier = 25214903917
increment = 11
modulus = pow(2, 48)

# a float is a number with decimals
# an integer is a whole number
# a boolean is true or false

def randomInt(): # range [0 to 2^48]
    global seed
    seed = (seed * multiplier + increment) % modulus
    return seed

def randomFloat(): # range [0 to 1]
    return (randomInt() / modulus)

def randomIntRange(min, max): # custom range [minimum, maximum]
    return (math.floor(randomFloatRange(min, max)))

def randomFloatRange(min, max): # custom range [minimum, maximum]
    return (min + randomFloat() * (max - min))

def randomBool(chance): # chance of getting true (example: randomBool(20) has a 20% chance of returning true)
    if(chance == 0):
        chance = 0.5
    return (randomFloat() < chance)


# execute functions and print results
print("Sequence of Random Integers between 0 and the Modulus")
print(randomInt())
print(randomInt())
print(randomInt())
print(randomInt())
print("\nSequence of Random Floats between 0 and 1")
print(randomFloat())
print(randomFloat())
print(randomFloat())
print(randomFloat())
print("\nSequence of Random Integers between 100 and 250")
print(randomIntRange(100, 250))
print(randomIntRange(100, 250))
print(randomIntRange(100, 250))
print(randomIntRange(100, 250))
print("\nSequence of Random Floats between 60 and 70")
print(randomFloatRange(60, 70))
print(randomFloatRange(60, 70))
print(randomFloatRange(60, 70))
print(randomFloatRange(60, 70))
print("\nSequence of Random Booleans with a chance of 30% of getting true")
print(randomBool(0.3))
print(randomBool(0.3))
print(randomBool(0.3))
print(randomBool(0.3))
