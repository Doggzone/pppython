def login(members):
    username = input("Enter your name: (4 letters max) ")
    while len(username) > 4:
        username = input("Enter your name: (4 letters max) ")
    trypasswd = input("Enter your password: ")
    if None: # username is in the key of members
        if None: # trypasswd is the same as username's password

            # Show the number of games played and the number of wins
            # Example: "You played 101 games and won 54 of them."
 
            # Show the winning percentage in percent
            # Example: "Your all-time winning percentage is 53.5%"

            # Show the number of chips the player has
            # Example : if the number is 5, "You have 5 chips."
            # Example : if the number is -5, "You owe 5 chips."
            return username, tries, wins, chips, members
        else:
            return login(members)
    else:
        # Add username to members dictionary.
        return username, 0, 0, 0, members