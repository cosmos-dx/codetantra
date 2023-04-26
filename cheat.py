import pyautogui,time
  
time.sleep(5)
  
# to display the time at which the message is sent
#f = open('cheat.txt', 'r')
#con = f.read()
#print(con)

#f.close()


with open(r"cheat.txt", 'r') as fp:
    # lines to read
    #line_numbers = [4, 7]
    # To store lines
    counter = -1;
    sp = ""
    lines = []
    data =[]
    for i, line in enumerate(fp):
        lines.append(line.strip())
        
    for linestr in lines:
        '''
        if(counter):
            for i in range(counter):
                sp += ""
            linestr = sp + linestr
        sp=""

        for word in linestr:
            if(word == '{'):
                counter += 1
            if (word == '}'):
                counter -= 1
        '''
        data.append(linestr)
    
print(data)
for i in range (1000):

    for i in data:
        #pyautogui.typewrite(i)
        pass
        #pyautogui.press("enter")

pyautogui.typewrite("code-by : cosmos_dx")

fp.close()
