import numpy as np
import matplotlib.pyplot as plt
import os
from data import data

# WINWEBSEC
winwebsec = {
        "mov": 159,
        "push": 41,
        "add": 20,
        "call": 17,
        "pop": 12,
        "sub": 9,
        "cmp": 7,
        "retn": 6,
        "jmp": 5,
        "jz": 3,
        "movzx": 3,
        "jnz": 3,
        "lea": 3,
        "xor": 3,
        "test": 2,
        "shr": 2,
        "jbe": 1,
        "jnb": 1,
        "imul": 1,
        "shl": 1,
        "jl": 1,
    }

# ZBOT
zbot = {
        "mov": 205,
        "push": 86,
        "add": 44,
        "call": 31,
        "jmp": 22,
        "pop": 13,
        "retn": 13,
        "sub": 9,
        "cmp": 8,
        "xor": 7,
        "lea": 7,
        "jz": 6,
        "test": 6,
        "jnb": 5,
        "movzx": 3,
        "jnz": 2,
        "shr": 1,
        "sar": 1,
        "and": 1,
        "jge": 1,
        "pusha": 1,
    }

# ZERO ACCESS
zeroaccess = {
        "mov": 2149,
        "xor": 500,
        "push": 414,
        "or": 308,
        "sub": 240,
        "cmp": 211,
        "add": 209,
        "and": 150,
        "shr": 119,
        "call": 114,
        "shl": 113,
        "adc": 93,
        "shrd": 89,
        "jmp": 83,
        "movzx": 80,
        "lea": 70,
        "sbb": 69,
        "imul": 67,
        "jnz": 58,
        "pop": 51,
        "div": 37,
        "jz": 34,
        "not": 27,
        "retn": 20,
        "dec": 20,
        "inc": 19,
        "jb": 17,
        "neg": 17,
        "leave": 14,
        "shld": 13,
        "ja": 11,
        "cdq": 11,
        "jnb": 11,
        "jbe": 9,
        "jge": 8,
        "test": 7,
        "mul": 7,
        "idiv": 6,
        "jle": 6,
        "jg": 6,
        "jl": 4,
        "rcr": 2,
        "xchg": 2,
        "rol": 1,
        "ror": 1,
    }

winwebsec_opcodes_ranked = {
    "A": ["mov"],
    "B": ["push", "add", "call", "pop"],
    "C": [
        "sub",
        "cmp",
        "retn",
        "jmp",
        "jz",
        "movzx",
        "jnz",
        "lea",
        "xor",
        "test",
        "shr",
        "jbe",
        "jnb",
        "imul",
        "shl",
        "jl",
    ],
}
zeroaccess_opcodes_ranked = {
    "A": ["mov", "xor", "push", "or", "sub", "cmp", "add", "and", "shr", "call", "shl"],
    "B": [
        "adc",
        "shrd",
        "jmp",
        "movzx",
        "lea",
        "sbb",
        "imul",
        "jnz",
        "pop",
        "div",
        "jz",
        "not",
        "retn",
        "dec",
        "inc",
        "jb",
        "neg",
        "leave",
        "shld",
        "ja",
        "cdq",
        "jnb",
    ],
    "C": [
        "jbe",
        "jge",
        "test",
        "mul",
        "idiv",
        "jle",
        "jg",
        "jl",
        "rcr",
        "xchg",
        "rol",
        "ror",
    ],
}
zbot_opcodes_ranked = {
    "A": ["mov"],
    "B": ["push", "add", "call", "jmp", "pop", "retn"],
    "C": [
        "sub",
        "cmp",
        "xor",
        "lea",
        "jz",
        "test",
        "jnb",
        "movzx",
        "jnz",
        "shr",
        "sar",
        "and",
        "jge",
        "pusha",
    ],
}

print("WINWEBSEC # OF OPCODES IN C: \n", len(winwebsec_opcodes_ranked["C"]), "\n")
print("ZBOT # OF OPCODES IN C: \n",len(zbot_opcodes_ranked["C"]), "\n")
print("ZEROACCESS # OF OPCODES IN B: \n",len(zeroaccess_opcodes_ranked["B"]), "\n")

path = "training-data/trainingset_zeroaccess.txt"
with open(path, "r") as y:
    read_data_zeroaccess = y.read()

list_zeroaccess = read_data_zeroaccess.split()
unique_zeroaccess = []
count_zeroaccess = 0
m_dist_zbot = {}
for i in list_zeroaccess:
    if i not in unique_zeroaccess:
        count_zeroaccess += 1
        unique_zeroaccess.append(i)   

for unique in unique_zeroaccess:
    x = data.counter(list_zeroaccess, unique)
    m_dist_zbot[unique]= x

plt.bar(m_dist_zbot.keys(), m_dist_zbot.values(), color='g') #winwebsec
plt.title("Zeroaccess Observation State Distribution")
# plt.show()
