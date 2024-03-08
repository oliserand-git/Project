#!/usr/bin/env python

print("I am from GitHub")

def reverse_complement(sequence):
    """Reverse complements a DNA sequence"""
    output = ""
    complement = {"A":"T", "T":"A", "G":"C", "C":"G"}
    for nt in sequence[::-1]:
        output += nt
    return output
