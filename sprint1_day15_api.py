import requests
import csv

API_URL="https://jsonplaceholder.typicode.com/users"

def fetch_data(url):
    url_data=requests.get(url)
    url_data.raise_for_status()
    return url_data.json()

def save_users(users,filename="users.csv"):
     with open(filename,"w",newline="",encoding="utf-8") as f:
          pen=csv.writer(f)
          pen.writerow(["id","name","username","email","phone","website"])
          for u in users:
               pen.writerow([
                    u.get("id"),
                    u.get("name"),
                    u.get("username"),
                    u.get("email"),
                    u.get("phone"),
                    u.get("website"),
               ]
               )

def main():
    """
    4) The main steps: get the users, show them on screen, then save them.
    """
    print("Getting users, please wait…")
    try:
        users = fetch_data(API_URL)
    except Exception as e:
        print("Could not get users:", e)
        return

    print("Here are the users we retrieved:")
    for u in users:
        print(f'  {u["id"]}: {u["name"]} ({u["email"]})')

    save_users(users)
    print("All user data saved to users.csv")

# 5) Only run main() when this file is executed directly,
#    not when it’s imported by another script.
if __name__ == "__main__":
    main()
