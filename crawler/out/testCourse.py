import json
with open('./allCourses.json','r') as courses:
    for line in courses:
        item=json.loads(line)
        #print item['link']
        try:        
            teacher_assistants=item['teacher_assistants']
        except:
            pass 
        try:               
            picture=item['picture']
        except:
            pass   
        try:
            term=item['term']
        except:
            pass   
        try:
            name=item['name']
        except:
            pass   
        try:
            professors=item['professors']
        except:
            pass   
        try:
            link=item['link']
        except:
            pass       
        