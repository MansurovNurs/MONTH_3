# import flet as ft


# def main(page: ft.Page):
#     page.title = "Hi Guys"

#     def change_name(e):
#         print(name_input.value)
    
#     name_input = ft.TextField(label="Enter word", on_change=change_name)
#     page.add(name_input)

#     def find_name(e):

#         friends = ["Tima", "Beka", "Adi"]

#         for name in friends:
#             if name == name_input.value.title():
#                 print(f'Name: {name}')  
#                 return
            

#     qwerty = find_name(change_name)
              
#     print(qwerty)

# ft.app(main)
import flet as ft

def main(page: ft.Page):
    page.title = "Hi Guys"

    friends = ["Tima", "Beka", "Adi"]

    def find_name(e):
        input_value = name_input.value.title()
        for name in friends:
            if name == input_value:
                print(f'drug: {name}')
                return
        print("Ne drug")

    name_input = ft.TextField(label="Enter word", on_change=find_name)
    page.add(name_input)

ft.app(main)
