"""
Author: Arham Islam
Date Created: March 24, 2025
"""

# copy-and-paste: python main.py following.txt followers.txt

import sys

def read_file(filename: str):
    """
    Reads a txt file of usernames and adds it to a list.

    Args:
        filename (string): Name of a txt file.
    
    Returns:
        list: List of usernames from a txt file.
    """
    usernames = []

    # Opens txt file
    f = open(filename, "r")

    # Iterates through txt file
    while True:
        # Reads each line of txt file
        username = f.readline().strip()

        # If 'username' is empty, then break out of loop
        if username == "":
            break

        # Adds 'username' into list
        usernames.append(username)
    
    f.close()

    return usernames

def match_usernames(following_usernames_list, followers_usernames_list):
    """
    Searches following and followers list and finds if an account that is being followed, does not follow the user back.

    Args:
        following_usernames_list (list): List of following account's usernames.
        followers_usernames_list (list): List of followers account's usernames.
    
    Returns:
        list: List of acccount's usernames that does not follow the user back.
    """
    not_following_back_list = []

    # loop through following list
    # check if following list index 0 is equal to followers list index 0
    # if it matches, then add it to a list (mutual)
    # if not, continue until one matches
    # if there is not a single match, then add it to a list (account not following user back)
    # for i in following_usernames_list:
    #     for j in followers_usernames_list:
    #         if(i == j):
    #             following_back_list.append(i)

    not_following_back_list = set(following_usernames_list) - set(followers_usernames_list)

    return not_following_back_list

def main():
    # Making sure user does not input incorrect format
    if len(sys.argv) < 3:
        print("Incorrect format, should be: python main.py <following txt file> <followers txt file>")
        sys.exit(1)

    # Files from user inputted arguments
    following_file = sys.argv[1]
    followers_file = sys.argv[2]

    # Reading both files
    following_usernames_list = read_file(following_file)
    followers_usernames_list = read_file(followers_file)

    # Searching both lists
    not_following_back_list = match_usernames(following_usernames_list, followers_usernames_list)

    # Printing account's usernames that do not follow the user back
    print("Accounts that don't follow you back:")
    for account in not_following_back_list:
        print(account)

main()