class chatbook:
    __user_id=0
    def __init__(self):
        self.id = chatbook.__user_id
        chatbook.__user_id+=1
        self.username = ''
        self.password = ''
        self.loggedin = False
        #self.menu()
    @staticmethod
    def getter():
        return chatbook.__user_id
    @staticmethod
    def setter(value):
        chatbook.__user_id=value

    def menu(self):
        user_input = input("""Welcome to Chatbook !! How would you like to proceed?'
                           1. Press 1 to signup
                           2. Press 2 to signin
                           3. Press 3 to write a post
                           4. Press 4 to message a friend
                           5. Press any other key to exit""")
        print("\n")
        if user_input =="1":
            self.signup()
        elif user_input =="2":
            self.signin()
        elif user_input =="3":
            self.post_msg()
        elif user_input =="4":
            self.sent_msg()
        else:
            exit()
    def signup(self):
        email=input("Setup your email here: ")
        pas =input("Setup Your Password here: ")
        self.username=email
        self.password=pas
        print("You have signed up successfully")
        print("\n")
        self.menu()
    def signin(self):
        if self.username =='' and self.password =='':
             print("You did not signup please signup first")
        else:
            username=input("Enter your user name: ")
            pas=input("Enter your password: ")
            if self.username ==username and self.password ==pas:
                print("You have signedin successfully!!")
                print("\n")
                self.loggedin=True
            else:
                print("Please input correct credentials")
        print("\n")
        self.menu()
    def post_msg(self):
        if self.loggedin:
            txt=input("Enter your post here: ")
            print(f"Following content has been posted {txt}")
        else:
            print("Please sign in first")
        print("\n")
        self.menu()
    def sent_msg(self):
        if self.loggedin:
            txt=input("Enter your message here: ")
            name=input("Whom to sent the message: ")
            print(f"Following message has been sent to {name} {txt}")
        else:
            print("Please sign in first")
        print("\n")
        self.menu()
    
