def timeConversionmethod(s):
    period = s[-2:]  # Last two characters (AM or PM)
    hour = int(s[:2])  # First two characters (hours)
    
    # If it's AM
    if period == "AM":
        if hour == 12:
            hour = 0
    else:
        if hour != 12:
            hour += 12
          
    return f"{hour:02}:{s[3:5]}:{s[6:8]}"
