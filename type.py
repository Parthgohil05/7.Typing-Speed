from time import time

def typeerror(prompt):
    global inwords
    
    words = prompt.split()
    errors = 0
    
    for i in  range(len(inwords)):
        if i in (0,len(inwords) -1):
            if inwords[i] == words[i]:
                continue
            else:
                errors = errors + 1
        else:
            if inwords[i] == words[i]:
                if(inwords[i+1] == words[i+1] and (inwords[i-1] == words[i-1])):
                     continue
                else:
                    errors += 1
            else:
                errors +=1
    
    return errors 



def speed(inprompt,stime,etime):
    global time
    global inwords
    
    inwords = inprompt.split()
    tword = len(inwords)
    speed = tword/time
    
    return speed

def elapsedime(stime,etime):
    time = etime - stime
    return time

if __name__=="__main__":
    prompt = "Able was I ere I saw Elba: This palindrome contains many common and less common letters, which can help you improve your precision."
    print(f" Type this: - {prompt} ")
    
    input("Press Enter when you are ready to check your speed ..!!! ")
    
    stime = time()
    inprompt = input()
    etime = time()
    
    
    time = round(elapsedime(stime,etime),2)
    speed = speed(inprompt,stime,etime)
    errors = typeerror(prompt)
    
    print("***************************************************************")
    print(f" Total time elapsed {time} seconds                          ")
    print(f" Your Average Typing speed was {speed} words per minute(w/m)")
    print(f" With the total of {errors} errors                          ")
    print("***************************************************************")
    
    