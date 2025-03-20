#Qs. 1. input=5  output = ["*****","*****","*****","*****","*****"]
def generate_square(n):
    """
    Function to return a square pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The size of the square.
    
    Returns:
    list: A list of strings where each string represents a row of the square.
    """
    # Your code here
    lst = []
    str = "*"*n
    for i in range(1,n+1):
        lst.append(str)
    return lst
    
print(generate_square(2))

#Qs. 2. input=5  output = ["*","**","***","****","*****"]
def generate_triangle(n):
    """
    Function to return a triangle pattern of '*' of height n as a list of strings.
    
    Parameters:
    n (int): The height of the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    # Your code here
    lst = []
    for i in range(1,n+1):
        lst.append("*"*i)
    return lst          #returning list of strings

print(generate_triangle(5))

#Qs. 3. input=5  output = ["    *","   **","  ***"," ****","*****"]
def generate_rhombus(n):
    """
    Function to return a rhombus pattern of '*' of size n as a list of strings.
    
    Parameters:
    n (int): The size of the rhombus.
    
    Returns:
    list: A list of strings where each string represents a row of the rhombus.
    """
    # Your code here
    lst = []
    for i in range(1,n+1):
        lst.append(" "*(n-i)+"*"*i)
    return lst          
print(generate_rhombus(5))

#Qs. 4. input=5  output = ["  *  "," *** ","*****"," *** ","  *  "]
def generate_diamond(n):
    """
    Function to return a diamond pattern of '*' of size n as a list of strings.
    
    Parameters:
    n (int): The size of the diamond.
    
    Returns:
    list: A list of strings where each string represents a row of the diamond.
    """
    # Your code here
    lst = []
    for i in range(1,n+1):
        lst.append(" "*(n-i)+"*"*i+" "*(n-i))
    for i in range(n-1,0,-1):
        lst.append(" "*(n-i)+"*"*i+" "*(n-i))
    return lst          
print(generate_diamond(5))

#Qs. 5. input=5 output = ["*****","*  *","*   *","*   *","*****"]
def generate_hollow_square(n):
    """
    Function to return a hollow square pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The size of the square.
    
    Returns:
    list: A list of strings where each string represents a row of the hollow square.
    """
    # Your code here
    lst = []
    for i in range(1,n+1):
        if i==1 or i==n:
            lst.append("*"*n)
        else:
            lst.append("*"+" "*(n-2)+"*")
    return lst          
print(generate_hollow_square(3))

#Qs. 6. input n=5,m=3 output = ["***","***","***","***","***"]
def generate_rectangle(n,m):
    """
    Function to return a rectangle pattern of '*' of size n*m as a list of strings.
    
    Parameters:
    n (int): The height of the rectangle.
    m (int): The width of the rectangle.
    
    Returns:
    list: A list of strings where each string represents a row of the rectangle.
    """
    # Your code here
    lst = []
    for i in range(1,n+1):
        lst.append("*"*m)
    return lst          
print(generate_rectangle(5,3))

#Qs. 7. input n=5 output = ["*","**","***","****","*****"]
def generate_left_triangle(n):
    """
    Function to return a left triangle pattern of '*' of height n as a list of strings.
    
    Parameters:
    n (int): The height of the left triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the left triangle.
    """
    # Your code here
    lst = []
    for i in range(1,n+1):
        lst.append("*"*i)
    return lst
print(generate_left_triangle(5))

#Qs. 8. input n=5 output = ["*****","****","***","**","*"]
def generate_right_triangle(n):
    """
    Function to return a right triangle pattern of '*' of height n as a list of strings.
    
    Parameters:
    n (int): The height of the right triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the right triangle.
    """
    # Your code here
    lst = []
    for i in range(1,n+1):
        lst.append("*"*(n+1-i))
    return lst
print(generate_right_triangle(5))

#Qs. 9. input n=5 output = ["  *  "," *** ","*****"]
def generate_isosceles_triangle(n):
    """
    Function to return an isosceles triangle pattern of '*' of height n as a list of strings.
    
    Parameters:
    n (int): The height of the isosceles triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the isosceles triangle.
    """
    # Your code here
    lst = []
    for i in range(1,n+1):
        lst.append(" "*(n-i)+"*"*(2*i-1)+" "*(n-i))
    return lst
print(generate_isosceles_triangle(5))

#Qs. 10. input n=5 output = ["*****"," *** ","  *  "]
def generate_reverse_pyramid(n):
    """
    Function to return a reverse pyramid pattern of '*' of height n as a list of strings.
    
    Parameters:
    n (int): The height of the reverse pyramid.
    
    Returns:
    list: A list of strings where each string represents a row of the reverse pyramid.
    """
    # Your code here
    lst = []
    for i in range(1,n+1):
        lst.append(" "*(i-1)+"*"*(2*(n-i)+1)+" "*(i-1))
    return lst
print(generate_reverse_pyramid(5))

#Qs. 11. input n=5 output = ["1","22","333","4444","55555"]
def generate_number_triangle(n):
    """
    Function to return a number triangle pattern as a list of strings.
    
    Parameters:
    n (int): The height of the number triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the number triangle.
    """
    # Your code here
    lst = []
    for i in range(1,n+1):
        lst.append(str(i)*i)
    return lst
print(generate_number_triangle(5))

#Qs. 12. input n=5 output = ["1","2 3","4 5 6","7 8 9 10","11 12 13 14 15"]
def generate_number_pyramid(n):
    """
    Function to return a number pyramid pattern as a list of strings.
    
    Parameters:
    n (int): The height of the number pyramid.
    
    Returns:
    list: A list of strings where each string represents a row of the number pyramid.
    """
    # Your code here
    lst = []
    count = 1
    for i in range(1,n+1):
        temp = ""
        for j in range(1,i+1):
            temp += str(count)+" "
            count += 1
        lst.append(temp.strip())
    return lst
print(generate_number_pyramid(5))

#Qs. 13. input n=5 output = ["  *  "," *** ","*****"," *** ","  *  "]
def generate_diamond_pattern(n):          
    """
    Function to return a diamond pattern of '*' of size n as a list of strings.
    """
    lst = []
    for i in range(1,n+1):
        lst.append(" "*(n-i)+"*"*(i+i-1)+" "*(n-i))
    for i in range(n-1,0,-1):
        lst.append(" "*(n-i)+"*"*(i+i-1)+" "*(n-i))
    return lst
print(generate_diamond_pattern(5))

#Qs. 14. input n=5 output = ["    *","    **","  ***"," ****","*****"]
def generate_inverted_rhombus(n):
    """
    Function to return an inverted rhombus pattern of '*' of size n as a list of strings.
    """
    lst = []
    for i in range(1,n+1):
        lst.append(" "*(n-i)+"*"*i)
    return lst
print(generate_inverted_rhombus(5))
  
#Qs. 15. input n=5 output = ["*****"," *** ","   *   "," *** ","*****"]
def generate_sandglass_pattern(n):
    """
    Function to return a sandglass pattern of '*' of size n as a list of strings.
    """
    lst = []
    for i in range(n,0,-1):
        lst.append(" "*(n-i)+"*"*(2*i-1)+" "*(n-i))
    for i in range(2,n+1):
        lst.append(" "*(n-i)+"*"*(2*i-1)+" "*(n-i))
    
    return lst
print(generate_sandglass_pattern(3))

#Qs. 16. input n=5 output = ["*","**","* *","*   *","*****"]
def generate_hollow_right_angled_triangle(n):
    """
    Function to return a hollow right-angled triangle of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The height of the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    lst = []
    for i in range(1,n+1):
        word = ""
        if i < 3:
             word = "*"*i
        elif i == n:
            word = "*"*i
        else:
            word = "*"*1+" "*(i-2)+"*"*1    
        lst.append(word)
    return lst
print(generate_hollow_right_angled_triangle(6))   

#Qs. 17. input n=5 output = ["*****","*  *","* *","**","*"]
def generate_hollow_inverted_right_angled_triangle(n):
    """
    Function to return a hollow inverted right-angled triangle of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The height of the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    # Your code here
    lst = []
    for i in range(n,0,-1):
        word = ""
        if i < 3:
             word = "*"*i
        elif i == n:
            word = "*"*i
        else:
            word = "*"*1+" "*(i-2)+"*"*1    
        lst.append(word)
    return lst
print(generate_hollow_inverted_right_angled_triangle(6))                

#Qs. 18. input n=4 output = ['   1   ', '  1 2  ', ' 1 2 3 ', '1 2 3 4']
def generate_number_pyramid(n):
    """
    Function to return a pyramid pattern of numbers of height n as a list of strings.
    
    Parameters:
    n (int): The height of the pyramid.
    
    Returns:
    list: A list of strings where each string represents a row of the pyramid pattern.
    """
    # Your code here
    lst = []
    for i in range(1, n + 1):
        row = " ".join(str(num) for num in range(1, i + 1))
        lst.append(row.center(n * 2 - 1))
    return lst
print(generate_number_pyramid(5))
 
#Qs. convert_centigrade_to_fahrenheit input=37 output=98.6
def convert_centigrade_to_fahrenheit(celsius):
    """
    Function to convert temperature in centigrade to fahrenheit.
    
    Parameters:
    celsius (float): The temperature in centigrade.
    
    Returns:
    float: The temperature in fahrenheit.
    """
    # Your code here
    return (celsius*9/5)+32
print(convert_centigrade_to_fahrenheit(37))      

#Qs. convert_fahrenheit_to_centigrade input=98.6 output=37
def convert_fahrenheit_to_centigrade(fahrenheit):
    """
    Function to convert temperature in fahrenheit to centigrade.
    
    Parameters:
    fahrenheit (float): The temperature in fahrenheit.
    
    Returns:
    float: The temperature in centigrade.
    """
    # Your code here
    return (fahrenheit-32)*5/9
print(convert_fahrenheit_to_centigrade(98.6))

#Qs. 21. number of rounds of lift where Two integers, n and capacity, where n is the total number of people, and capacity is the maximum number of people the lift can carry in one round.
def number_of_lift_rounds(n, capacity):
    """
    Function to calculate the number of rounds of a lift for a given number of people and capacity.
    
    Parameters:
    n (int): The total number of people.
    capacity (int): The maximum number of people the lift can carry.
    
    Returns:
    int: The number of rounds required to transport all the people.
    """
    # Your code here
    return (n + capacity - 1) // capacity        
print(number_of_lift_rounds(10, 3))

#Qs. 22. You are given the slope m and the y-intercept b of a line, along with a value x. Your task is to calculate and return the value of y using the equation of a line in slope-intercept form:
def calculate_y(slope, intercept, x):
    """
    Function to calculate the value of y using the slope-intercept form of a line.
    
    Parameters:
    slope (float): The slope of the line.
    intercept (float): The y-intercept of the line.
    x (float): The value of x for which y needs to be calculated.
    y=mx+b where m=slope and b=intercept
    Returns:
    float: The calculated value of y.
    """
    # Your code here
    return slope*x + intercept
print(calculate_y(2, 4, 3))

#Qs. 23. check list items are unique or not
def is_unique(lst):
    """
    Function to check if all elements in a list are unique.
    
    Parameters:
    lst (list): A list of elements.
    
    Returns:
    bool: True if all elements are unique, False otherwise.
    """
    # Your code here
    seen = set()
    for i in lst:
        if i in seen:
            return False
        seen.add(i)
    return True
print(is_unique([1, 2, 3, 4, 5,2,1,2,2]))

#Qs. 24. find  the maximum difference between any two consecutive numbers in a list.
def find_max_difference(lst):
    """
    Function to find the maximum difference between any two consecutive numbers in a list.
    
    Parameters:
    lst (list): A list of integers.
    
    Returns:
    int: The maximum difference between any two consecutive numbers in the list.
    """
    # Your code here
    max_diff = 0
    for i in range(1, len(lst)):
        diff = lst[i] - lst[i-1]
        if diff > max_diff:
            max_diff = diff
    return max_diff
print(find_max_difference([1, 20, 30, 14, 52]))

def max_consecutive_diff(lst):
    """
    Function to find the maximum difference between any two consecutive numbers in a list.
    
    Parameters:
    lst (list): A list of integers.
    
    Returns:
    int: The maximum difference between any two consecutive numbers in the list.
    """
    # Your code here
    if len(lst) < 2:
        return 0
    return max([abs(lst[i] - lst[i+1]) for i in range(len(lst)-1)])
print(max_consecutive_diff([11, 22, 13, 24, 5]))

#Qs. 25. find the age of a person given the birth date and the current date.
def calculate_age(birth_date, current_date):
    """
    Function to calculate the age of a person given their birth date and the current date.
    
    Parameters:
    birth_date (datetime.date): The birth date of the person.
    current_date (datetime.date): The current date.
    
    Returns:
    int: The age of the person in years.
    """
    # Your code here
    age = current_date.year - birth_date.year
    if current_date.month < birth_date.month or (current_date.month == birth_date.month and current_date.day < birth_date.day):
        age -= 1
    return age  
import datetime
print(calculate_age(datetime.date(1996, 8, 4), datetime.date(2025, 3, 20)))
