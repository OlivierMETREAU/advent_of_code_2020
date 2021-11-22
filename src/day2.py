import re

def day2(list_of_rules_and_passwords, new_policy=False):
    number_of_valid_password = 0
    for rule_with_password in list_of_rules_and_passwords:
        m = re.search(r'(\d+)-(\d+)\s+(\w):\s+(\w+)', rule_with_password)
        if not new_policy:
            occurence = m.group(4).count(m.group(3))
            if int(m.group(1)) <= occurence <= int(m.group(2)):
                number_of_valid_password += 1
        else:
            if (m.group(4)[int(m.group(1)) - 1] == m.group(3)) ^ (m.group(4)[int(m.group(2)) - 1] == m.group(3)):
                number_of_valid_password += 1
    return number_of_valid_password

def main():
   f = open("input_day2.txt", "r")
   lines = f.readlines()
   print(day2(lines, new_policy=True))

if __name__ == "__main__":
   main()