import re

def return_date_email(text):
    dates=set(re.findall(r"\d{4}-\d{2}-\d{2}",text))
    emails = set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text))

    return dates, emails

def main():

    with open("sample.log","r", encoding="utf-8") as f:
        text=f.read()
    
    dates, emails=return_date_email(text)

    with open("emails.txt", "w", encoding="utf-8") as newf:
        for email in emails:
            newf.write(f'{email}\n')

    with open("dates.txt", "w", encoding="utf-8") as newf:
        for date in dates:
            newf.write(f'{date}\n')


    print(f"Found {len(emails)} unique emails and {len(dates)} unique dates.")

if __name__ == "__main__":
    main()
