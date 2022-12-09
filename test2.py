while True:
    query=input("test me!: ")

    check=0; checking=True
    while checking:
        try:
            for chara in query:
                if chara == ".":
                    check+=1
                
                else:
                    for num in "1234567890":
                        if (chara == num):
                            check+=1

            if(len(query)==check):
                query=float(query)
            checking=False

        except:
            continue

    print(type(query))