def loading_bar(loading_percent):
    percent_bar = "%" * (loading_percent // 10) + "." * (10 - loading_percent // 10)
    if loading_percent != 100:
        return f"{loading_percent}% [{percent_bar}]\nStill loading..."
    return f"{loading_percent}% Complete!\n[{percent_bar}]"


percentage = int(input())
print(loading_bar(percentage))