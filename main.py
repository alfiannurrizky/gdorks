try:
    from googlesearch import search
    import time
    import argparse
    from colorama import Fore
except ImportError: 
    print("No module named 'google' found")
    
#just simple banner
def banner():
    txt = ("""
 ░▒▓██████▓▒░░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓███████▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
░▒▓█▓▒▒▓███▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓███████▓▒░ ░▒▓██████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░ 
 ░▒▓██████▓▒░░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░  
                                                                            v1.0 """)
    
    author = ("""
 Author:  Alfian Nurrizky
 Github:  https://github.com/alfiannurrizky
 Linkedin: https://www.linkedin.com/in/alfian-nurrizky/ \n\n""")
    print(txt)
    print(author)

#function for send request to google    
def query(domain, payload, take):
    counter = 0
    for result in search("site:" + domain +" "+  payload, num=int(take), stop=int(take), pause=5):
        counter += 1
        
        print(f"[+]{Fore.CYAN} {counter}. Payload {payload} -> {result}")
        
        time.sleep(0.1)
                
        if counter == int(take):
            print("\n")
            break
                
        time.sleep(0.1)

 
def dorking():
    banner()

    try:
        print("Finding Target...")
        
        #flag arguments
        parser = argparse.ArgumentParser()
        parser.add_argument("-d", "--domain", help="Input domain e.g google.com")
        parser.add_argument("-t", "--take", help="Number of result you want")
        args = parser.parse_args()
        parser.parse_args()
        
        if not args.domain and not args.take:
            parser.error("Please provide either the -d option and the -t option.")
        elif not args.domain:
            parser.error("Please provide either the -d option")
        elif not args.take:
            parser.error("Please provide either the -t option")
        
        # read line by line in payload.txt
        count = 0
        file1 = open('payload.txt', 'r')
        lines = file1.readlines()
        
        for line in lines:
            count += 1
            payload = line.strip()
        
        # call query function for send request url to google with payload given in txt file.
            query(args.domain, payload, args.take)
            
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    dorking()
        
