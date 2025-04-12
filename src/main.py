import flet as ft

def main(page: ft.Page):
    page.title = "Hi Guys"

    def click_button(e):

        age = int(age_input.value)
    

        data_list.append(hobby_input.value)
        personal_data.append({'name': name_input.value, 'age':age})
                  

        print(f':\nPersonal data: \n{personal_data}\n Hobbies: {data_list}')




    name_input = ft.TextField(label="Enter name: ")
    hobby_input = ft.TextField(label='Enter hobby: ')
    age_input = ft.TextField('only numbers', label='Enter age: ')
    
    
          
    
    data_list = []
    personal_data = []

    button = ft.ElevatedButton("Save it", on_click=click_button)
    page.add(name_input, age_input, hobby_input, button)


ft.app(main)


