def hamming_distance(s1, s2):
    #ensure the strings are of equal length
    if len(s1) != len(s2):
        raise ValueError("Strings must be of equal length")
    #count different positions
    return sum(el1 != el2 for el1, el2 in zip(s1, s2))
#example usage
s1="karolin"
s2="kathrin"
distance = hamming_distance(s1, s2)
print(f"Hamming distance between '{s1}' and '{s2}' is: {distance}")

#jackcard distance
def jaccard_distance(s1, s2):
    #convert strings to sets
    set1 = set(s1)
    set2 = set(s2)
    #calculate intersection and union
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    #calculate jaccard distance
    return 1 - intersection / union if union != 0 else 0

#example usage
s1="karolin"
s2="kathrin"
distance = jaccard_distance(s1, s2)
print(f"Jaccard distance between '{s1}' and '{s2}' is: {distance}")

