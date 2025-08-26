# python 關鍵字參數 keyword arguments

def hello1(greeting,title,firstname,lastname):
    print(f"{greeting} {title} {firstname} {lastname}")

hello1("hi~","Manager","Cindy",lastname="lin")

def get_phone(country_code,area_code,first,last):
    return (f"{country_code}-{area_code}-{first}-{last}")

str=get_phone(
    country_code="886",
    area_code="02",
    first="0922",
    last="7894"
)
print(str)



