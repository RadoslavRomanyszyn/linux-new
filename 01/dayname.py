#!/usr/bin/env python3
from datetime import date

def main():
    current_date = date.today()
    current_day_name = current_date.strftime("%A")
    print(current_day_name)

if __name__ == '__main__':
    main()
