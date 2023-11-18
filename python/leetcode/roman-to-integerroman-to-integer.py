def romanToInt(s):
    roman_to_int = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    for char in s:
        curr_value = roman_to_int[char]
        total += curr_value
        
        if curr_value > prev_value:
            total -= 2 * prev_value
        
        prev_value = curr_value
    
    return total
print(romanToInt("MCMXCIV"))