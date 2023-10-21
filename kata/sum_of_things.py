
def sumitup(vals):
    sum = 0
    for s in vals:
        if s.isdigit() and len(s) > 1:
            sum += int(s)
        elif s.startswith('0x'):
            sum += int(s, base=16)
        elif s.startswith('0o'):
            sum += int(s, base=8)
        elif s.startswith('0b'):
            sum += int(s, base=2)
        else:
            sum += ord(s)
    return sum
def main():
    while(True):
        try:
          inp = input()
          if len(inp) == 0: break
          print(sumitup(inp.split()))
        except:
            break
    return 0

if __name__ == "__main__":
    main()