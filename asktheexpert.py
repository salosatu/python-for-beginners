from tkinter import Tk, simpledialog, messagebox

def read_from_file():
    with open('capital.txt') as file:
        for line in file:
            line = line.rstrip('\n')
            country, city = line.split('/')
            the_world[country] = city

def write_to_file(country_name, city_name):
    with open('capital.txt', 'a') as file:
        file.write('\n' + country_name + '/' + city_name)


print("Ask the expert - World's capitals")
root = Tk()
root.withdraw()
the_world = {}
read_from_file()

while True:
    query_country = simpledialog.askstring('World', 'Write the name of a country')
    query_country = query_country.capitalize()

    if query_country in the_world:
        result = the_world[query_country]
        messagebox.showinfo('Answer', 
                            "World's " + query_country + ' capitol is ' + result + '!')
    else:
        new_city = simpledialog.askstring('Teach me', 
                                        "I don't know! " +
                                        "What's the capitol in country " + query_country + '?')
        the_world[query_country] = new_city
        write_to_file(query_country, new_city)
