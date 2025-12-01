# __ Message Class__

class Message:
  
  message_counter = 1   # simple counter 
  
  def __init__(self, sender, content):
    self.sender = sender
    self.content = content
    self.id = Message.message_counter
    Message.message_counter +=1
    
  def __str__(self):
    return f" {self.id} : {self.sender} :{self.content}"  
  
# __Chatroom Class__
  
class Chatroom:
  
  def __init__(self, name):
    self.name = name
    self.users = []
    self.messages = []
    
  def __str__(self):
        return self.name
    
  def add_user(self, user):
    self.users.append(user)
  
  def remove_user(self, user):
    self.users.remove(user)
  
  def broadcast(self, sender, content):
    message = Message(sender, content)
    self.messages.append(message)
    print(message)
    
  def chat_history(self):
    for msg in self.messages:
      print(msg.content)
      
# __User Class__ 

class User:
  
  def __init__(self, username):
    self.username = username 
    self.chatroom = None
    
  def __str__(self):
        return self.username
    
  def join_chatroom(self, chatroom):  # chatroom --> object 
    
    if self.chatroom:
      print(f"{self.username} is already in the classroom")
     
    else:
      chatroom.add_user(self)
      self.chatroom = chatroom
      print(f"{self.username} joined {self.chatroom}")
      
  def leave_chatroom(self):
    
    if not self.chatroom:
      print(f"{self.username} is not in the classroom")
    else:
      self.chatroom.remove_user(self)
      print(f"{self.username} left {self.chatroom}")
      
  def send_messages(self, content):
    if not self.chatroom:
      print(f"{self.username} cannot send the message")
      
    else:
      self.chatroom.broadcast(self, content)

room = Chatroom("Python Lounge") 
  
u1 = User("Alice")
u1.join_chatroom(room)
u1.send_messages("heyy How are you")
room.chat_history()