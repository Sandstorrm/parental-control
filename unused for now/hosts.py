import os

HOSTS_PATH = r"C:\Windows\System32\drivers\etc\hosts"

def add_website(website):
    with open(HOSTS_PATH, 'a') as file:
        file.write(f"10.0.0.1 {website}\n")
    print(f"{website} has been added to the hosts file.")

def remove_website(website):
    lines = []
    website_found = False
    with open(HOSTS_PATH, 'r') as file:
        lines = file.readlines()

    with open(HOSTS_PATH, 'w') as file:
        for line in lines:
            if line.startswith(f"10.0.0.1 {website}"):
                website_found = True
            else:
                file.write(line)

    if website_found:
        print(f"{website} has been removed from the hosts file.")
    else:
        print(f"{website} was not found in the hosts file.")

def list_blocked_websites():
    blocked_websites = []
    with open(HOSTS_PATH, 'r') as file:
        lines = file.readlines()
        blocked_websites = [line.split()[1] for line in lines if line.startswith("10.0.0.1")]

    print("Blocked websites:")
    for website in blocked_websites:
        print(website)

def main():
    while True:
        action = input("HOSTS: ")

        if action == "/exit":
            break

        if action.startswith("/add"):
            parts = action.split()
            if len(parts) > 1:
                website = parts[1]
                add_website(website)
            else:
                print("Please provide a website to add.")
        elif action.startswith("/rem"):
            parts = action.split()
            if len(parts) > 1:
                website = parts[1]
                remove_website(website)
            else:
                print("Please provide a website to remove.")
        elif action == "/list":
            list_blocked_websites()
        else:
            print("Invalid action. Please enter '/add {website}', '/rem {website}', '/list', or '/exit'.")

if __name__ == "__main__":
    main()