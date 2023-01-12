def convert(number):
    '''Converts a number into a string containing raindrop sounds if it has factors of 
    3, 5 and/or 7.

    Parameters
    number: int
        detail

    3 as a factor, add 'pling' to the result
    5 as a factor, add 'plang' to the result
    7 as a factor, add 'plong' to the result
    3, 5, or 7 are not factors, output the digits as a string
    '''
    raindrops = ''
    
    # Check if the number has factors of 3, 5, and 7
    is_factor3 = number % 3 == 0
    is_factor5 = number % 5 == 0
    is_factor7 = number % 7 == 0

    # Logic to output result
    if is_factor3:
        raindrops = 'Pling'
    if is_factor5:
       raindrops += 'Plang'
    if is_factor7:
       raindrops += 'Plong'
    if not raindrops:
        return str(number)
    else: return raindrops