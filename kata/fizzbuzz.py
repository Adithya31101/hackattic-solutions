def fizzbuzz(n, m):
    for num in range(n, m+1):
        if num % 15 == 0:
            print('FizzBuzz')
        elif num % 3 == 0:
            print('Fizz')
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

def main():
    while(True):
        try:
          inp = input()
          if len(inp) == 0: break
          inp_split = inp.split()
          n = int(inp_split[0])
          m = int(inp_split[1])
          fizzbuzz(n, m)
        except:
            break
    return 0

if __name__ == "__main__":
    main()