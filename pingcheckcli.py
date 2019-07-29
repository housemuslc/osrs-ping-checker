import requests
import re
from bs4 import BeautifulSoup
from ping3 import ping


def main():
    worlds = getworlds()
    pingservers(worlds)

def getworlds():
    worldlist = {}
    try:
        print("[*] Retreiving worlds...")
        worlds = requests.get("http://oldschool.runescape.com/slu")
        soup = BeautifulSoup(worlds.text, 'html.parser')
        for world in soup.find_all('a', 'server-list__world-link'):
            worldlist[int(world['id'][10:])] = (world.contents[0].replace(" ", "")) + '.runescape.com'
        print("[+] Retreived worlds!")
    except:
        print("[-] Couldn't retreive web page. Please check your connection.")
    return sorted(worldlist.items(), key=lambda t: int(t[0]))

def pingservers(worldlist):
    results = {}
    for world, address in worldlist:
        print("[*] Pinging World " + str(world))
        ms = str(ping(address, unit='ms'))
        results[world] = float(ms)
    print("[+] Ping checks complete!")
    logresults(results)

def logresults(results):
    sortedresults = sorted(results.items(), key=lambda t: t[1])
    lowest = next(iter(sortedresults))
    print("[+] The least amount of ping is world %s with %.2fms ping\n\
[+] All results logged to text file: \"results.txt\"" % (lowest[0], lowest[1]))
    output = open('results.txt', 'a')
    for item in sortedresults:
        output.write(str(item) + "\n")
    output.close()

if __name__=="__main__":
    main()