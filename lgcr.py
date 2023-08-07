def loging():

    print("welcom to Psada loging screen !")
    nom = input("input your name")
    passe = input("input your password")
    if nom=='kali':
        if passe == "kali":
            print("connected as " + str(nom))
            
        else:
            print("bad password try again")
            loging()

    else:
        print("bad name try again")
        loging()
    
def main():
    loging()





if __name__ == "__main__":
    main()