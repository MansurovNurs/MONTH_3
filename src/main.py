import flet as ft

def main(page: ft.Page):
    page.title = "Hi Guys"


    title = ft.Text(value="Info", size=30, weight=ft.FontWeight.BOLD)
    
    def click_button(e):

        age_text = age_input.value.strip()
    
        if not age_text.isdigit():
            print('only numbers!')
            return

        age = int(age_text)

        if age <= 0:
            print('age must be positive!')
            return
        

        elif 0 <= age <= 18:
            age_color = ft.Colors.BLUE

        elif 19 <= age <= 25:
            age_color = ft.Colors.GREEN

        elif 26 <= age <= 40:
            age_color = ft.Colors.GREY_400
            
        else: 
            age_color = ft.Colors.RED



        data = f"name:{name_input.value} age: {age_input.value} hobby: {hobby_input.value}"
       
        list.controls.append(ft.Text(value=data, size=20, color=age_color, bgcolor=ft.Colors.DEEP_ORANGE_50))
        
        
        page.update()

    name_input = ft.TextField(label="Enter name: ")
    age_input = ft.TextField(label='Enter age: ')
    hobby_input = ft.TextField(label='Enter hobby:  ')
    
    list = ft.Column()
          

    button = ft.ElevatedButton("Save it", on_click=click_button, bgcolor=ft.Colors.BROWN_800, color=ft.Colors.AMBER_800)
    page.add(title, name_input, age_input, hobby_input, button, list)


ft.app(main)


