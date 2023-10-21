import json
def get_balance(obj):
    if "extra" in obj:
        return get_balance(obj['extra'])
    elif 'balance' in obj:
        return obj['balance']
    elif obj.values():
        return get_balance(list(obj.values())[0])
    else: return 0
def print_comma(amt):
    final = ""
    count = 0
    for i in range(len(amt) - 1, -1, -1):
        if count % 3 == 0 and count != 0:
            final = amt[i] + "," + final
        else:
            final = amt[i] + final
        count += 1
    return final

def sortjson(jsonobjs):
    data = []
    for js in jsonobjs:
        d = json.loads(js)
        data.append({ "name": list(d.keys())[0], "balance": get_balance(d) })
    data = (sorted(data, key=lambda d: d['balance']))
    for d in data:
        print(f"{d['name']}: {print_comma(str(d['balance']))}")

def main():
    jsonobjs = []
    while(True):
        try:
          inp = input()
          if len(inp) == 0: break
          jsonobjs.append(inp)
        except:
            break
    sortjson(jsonobjs)
    return 0

if __name__ == "__main__":
    main()