results = ["Mario", "Luigi", "Princess", "Yoshi", "Koopa Troopa", "Toad", "Bowser", "Donkey Kong Jr"]
    
#results.remove("Bowser")
#results.insert(0,"Bowser")
#results.reverse()
for i in range(len(results)):
    updated_results = results [i:] + results[:i]
    print (updated_results)


