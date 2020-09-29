import sys
import json

first_name = " "
lname = " "
email = " "
phone = " "
command = sys.argv[1]


def add_person():
    try:
        file = open('db.json', 'r')
        previous_content = json.loads(file.read())
        file.close()

        previous_content.extend(content)

        file = open('db.json', 'w')

        file.write(json.dumps(previous_content))
        file.close()

    except:
        file = open('db.json', 'w')
        file.write(json.dumps(content))
        file.close()

def print_usage():
    print(
        "db -a [fname] [lname] [phone] [email]   (add a new record)"
        "db -f [search]     (find and show th efirst record that matches the search"
        "db -l              (list all records)"
        "db - d [search]    (delete the first record that matches the search)"
    )


def search(search_string):
    content = load_content()
    search_string = sys.argv[2].lower()
    for c in content:
        if search_string == c.lower(['first_name'] or c[lname]):
            print(c)
        else:
            print("No items matching the search.")


def load_content():
    file = open('db.json', 'r')
    content = json.loads(file.read())
    file.close()
    return content


def save_content(content: list):
    file = open('db.json', 'w')
    file.write(json.dumps(content))
    file.close()


def delete(search_string):
    content = load_content()
    search_string = sys.argv[2].lower()
    for c in content:
        if search_string == c.lower(['first_name'] or c['lname']):
            print(c + " was deleted.")
            del(c)
        else:
            print("No items matching the search.")
    # searched_names = [person["fist_name"] + person["last_name"] for person in people if person["first_name"] == searchString or person["last_name"] == search_string]
    # print(str(people[searched_names[0]]) + " was deleted.")
    # del people[searched_names[0]]

def print_people(people: list):
    pass


if command == '-a' and len(sys.argv) > 2: #for f and d
    first_name = sys.argv[2]
    lname = sys.argv[3]
    email = sys.argv[4]
    phone = sys.argv[5]
    content = [
        {
            'first_name': first_name,
            'lname': lname,
            'email': email,
            'phone': phone
         }
    ]
    print("{} {} was added.".format(first_name, lname))

    add_person()

elif command =='-l':
    content = load_content()
    for c in content:
        print(c['first_name'])
        print(c['lname'])
        print(c['email'])
        print(c['phone'])
        print('--------------------------------')

elif command == '-d' and len(sys.argv) > 2:
    content = load_content()

    for c in content:
        if sys.argv[2].lower() == c['first_name'].lower() or sys.argv[2].lower() == c['lname'].lower():
            content.remove(c)
            print('Deleted: \n')
            print(c['first_name'])
            print(c['lname'])
            print(c['email'])
            print(c['phone'])
            print('--------------------------------')
            break


    save_content(content)
elif command == '-f' and len(sys.argv) > 2:
    content = load_content()

    for c in content:
        if sys.argv[2].lower() == c['first_name'].lower() or sys.argv[2].lower() == c['lname'].lower():
            print(c['first_name'])
            print(c['lname'])
            print(c['email'])
            print(c['phone'])
            print('--------------------------------')
            break


else:
    print_usage()