def main():
    with open("result_summary3.txt") as f:
        lines = f.read().splitlines()
    
    total = 0
    kv = {}
    for l in lines:
        label, count = l.split()[0:2]
        kv[label] = int(count)
        total += int(count)

    cdf = 0.0
    buffer = []
    with open("result_summary4.txt", mode='w') as f:
        for k,v in kv.items():
            cdf += int(v)/total
            f.write(f"{k} {cdf}\n")

if __name__ == "__main__":
    main()
