def display_msg(m):
  print(m)

def ask_ques(q):
    resp = input(q)
    return resp
  

if __name__ == '__main__':
   resp = ask_ques("What is your favorite candy? ")
   display_msg(f"Wow... I love {resp} too")