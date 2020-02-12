#def calculate_average(a, b):
      # Calculate an average of two numbers 
      
 #     result = (a + b) / 2
#    return result
  
#x = 45
#y = 56
 
#average = calculate_average(x, y)
#print(average)

#def print_hello():
 #   print("Hello!")
  
  
#def print_goodbye():
 #   print("Bye!")
  
  
#def main():
 #   print_hello()
 #  print_goodbye()
 
#if __name__ == "__main__":
 #   main()

def a(my_list):
    print("function a, list =  ", my_list)
    my_list = [10, 20, 30]
    print("function a, list =  ", my_list)
 
my_list = [5, 2, 4]
  
print("global scope, list =", my_list)
a(my_list)
print("global scope, list =", my_list)