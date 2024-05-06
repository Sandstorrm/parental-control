import json, datetime, os

def load_settings():
    if os.path.exists('settings.json'):
        with open('settings.json', 'r') as f:
            return json.load(f)
    else:
        return {}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def Count():
    count = 0
    if not os.path.exists(points_file):
        with open(points_file, 'w', encoding='utf-16'):
            print('Points file created.')

    with open(points_file, 'r', encoding='utf-16') as file:
        for line in file:
            if current_date in line:
                count += 1
    return count


settings = load_settings()
expected_points = settings['threshold']
points_file = settings['points_file']
current_date = datetime.datetime.now().strftime("%m/%d/%y")

clear_screen()
print(f'Points: {Count()}/{expected_points}')

while True:
    command = input('PC> ')
    if command == '/points':
        print(f'Points: {Count()}/{expected_points}')
    elif command == '/hosts':
        exec(open('hosts.py').read())
    elif command == '/settings':
        exec(open('settings.py').read())
    elif command == '/exit':
        break
    else:
        print("Invalid command. Please enter /points, /hosts, /settings or /exit.")