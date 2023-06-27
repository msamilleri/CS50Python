def grocery():
    market_deposite={}
    while True:
        try:
            item=input().upper()

        except EOFError:
            break
        else:
            if item in market_deposite:
                market_deposite[item]+=1
            else:
                market_deposite[item]=1
    sorted_items = dict(sorted(market_deposite.items()))
    for item, count in sorted_items.items():
        print(count, item)

grocery()

