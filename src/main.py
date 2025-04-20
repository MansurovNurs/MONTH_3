import flet as ft

def main(page: ft.Page):
    page.title = "Hi Guys"


    title = ft.Text(value="Info", size=30, weight=ft.FontWeight.BOLD)

  
    total_age_text = ft.Text(value='total age: 0', size=20, weight=ft.FontWeight.BOLD)
    
    def click_button(e):
        total_age = 0

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
            age_color = ft.Colors.RED
            
        else: 
            age_color = ft.Colors.BLACK

        total_age += age
        total_age_text.value = f'total age: {total_age}'


       
        list.controls.append(
            ft.Row(
                controls=[
                    ft.Text(value=f'name: {name_input.value} |', size=20, color=ft.colors.BLACK, bgcolor=ft.Colors.DEEP_ORANGE_50),
                    ft.Text(value=f'age: {age_input.value} |', size=20, color=age_color, bgcolor=ft.Colors.DEEP_ORANGE_50),
                    ft.Text(value=f'hobby: {hobby_input.value}', size=20, color=ft.Colors.BLACK, bgcolor=ft.Colors.DEEP_ORANGE_50),
                    ft.IconButton(icon=ft.icons.EDIT, icon_size=20, icon_color=ft.colors.BROWN),
                    ft.IconButton(icon=ft.icons.DELETE_OUTLINE, icon_size=20, icon_color=ft.colors.RED)
                ] 
            )
        )
        name_input.value = ""
        age_input.value = ""
        hobby_input.value = ""

        page.update()

    name_input = ft.TextField(label="Enter name: ")
    age_input = ft.TextField(label='Enter age: ')
    hobby_input = ft.TextField(label='Enter hobby:  ')
    # icons = ft.icons.ACCESS_TIME
    
    list = ft.Column(
        expand=True, scroll="alweys"
    )
          

    button = ft.ElevatedButton("Save it", on_click=click_button, bgcolor=ft.Colors.BROWN_800, color=ft.Colors.AMBER_800)
    row_area = ft.Row(
        controls=[name_input, age_input, hobby_input, button]
    )

    

    page.add(title, row_area, total_age_text, list)


ft.app(main)


