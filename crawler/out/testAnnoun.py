import json
with open('./annoncements.json','r') as courses:
    for line in courses:
        item=json.loads(line)
        #print item['link']
        
        annons=item['annons']
        anonsSplitter="**********" #10 ta *
        dateSplitter="||||||||||" #10 ta \
        annoncements=annons.split(anonsSplitter)
        
        #now we have announcements in annoncements list
        for annon in annoncements:
			try:
	            date=annon.split(dateSplitter)[0]
			except:
				date=""
            try:            
                context=annon.split(dateSplitter)[1]
            except:
                context=""
            #print context
            
            
