from plyer import notification

def Notification(title,message,timeout):
    notification.notify(title=title,message=message,timeout=timeout)

if __name__ == "__main__":
    inp1 = input("Enter the Heading\n")
    inp2 = input("Enter the Message\n")
    inp3 = input("Enter how many seconds the Notification should stay")
    Notification(inp1,inp2)    
