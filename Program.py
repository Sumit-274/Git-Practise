from plyer import notification

def Notification(title,message):
    notification.notify(title=title,message=message)

if __name__ == "__main__":
    inp1 = input("Enter the Heading\n")
    inp2 = input("Enter the Message\n")
    Notification(inp1,inp2)    
