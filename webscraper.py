#Importing all the necessary parts
import requests
from bs4 import BeautifulSoup as bs
names = {}
prices = []
stock = []
def sortPrice(GPUdict, y, r, stock2):
        #Writing the result to a file
        f = open("results.txt","w")
        n = 0
        if r == "h":
            x = ({k: v for k, v in sorted(GPUdict.items(), key=lambda item: item[1], reverse=True)})
        else: 
            x = ({k: v for k, v in sorted(GPUdict.items(), key=lambda item: item[1])})
        for key,value in x.items():
            if int(y) > n:
                n += 1
                #Printing and writing the result to a file
                print(key +" "+ str(value))
                f.write(key +" "+ str(value)+" €"+"\n")
        f.close()
#Defining the actual scraper function
def GPUScraper():
    page = 1
    page2 = 1
    page3 = 1
    n = 0
    z = 0
    #Getting all the price data and appending it to a list
    while page2 != 5:
        url2 = f"https://www.jimms.fi/fi/Product/List/000-00P/komponentit--naytonohjaimet?p="+str(page2)+"&i=100&ob=7"
        r2 = requests.get(url2)
        src2 = r2.content
        soup2 = bs(src2, "html.parser")
        for div2 in soup2.find_all("div", class_="p_price"):
            #Removing the whitespaces from the GPU price for a cleaner look
                s = div2.get_text(strip=True).replace('\xa0', '').replace(",",".").replace("€","")
                price = float(s)
                prices.append(price)
        page2 = page2 + 1
    #Getting all the GPU data and appending it to a dictionary
    while page != 5:
        url = f"https://www.jimms.fi/fi/Product/List/000-00P/komponentit--naytonohjaimet?p=+"+str(page)+"&i=100&ob=7"
        r = requests.get(url)
        src = r.content
        soup = bs(src, "html.parser")
        for div in soup.find_all("div", class_="p_name"):
            names.update({div.get_text(strip=True) : prices[n]})
            n = n+1
        page = page + 1
def main():
    #Asking the user for their inputs
    GPUScraper()
    print("Do you want to sort the GPUs based on highest or lowest price? (h/l)")
    highOrLow = input()
    print("How many GPUs do you want to see? (0-374)")
    howMany = input()
    #Sorting the GPUs based on the users inputs
    sortPrice(names,howMany,highOrLow, stock)
if __name__ == '__main__':
    main()
    
    