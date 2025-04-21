import flet as ft

def main(page: ft.Page):
    page.title = "Hi Guys"

    page.total_expences = 0
    # page.counter = 0
    title = ft.Text(value="Info", size=30, weight=ft.FontWeight.BOLD)

    total_expences_text = ft.Text(value='total expences: 0', size=20, weight=ft.FontWeight.BOLD)
    def click_button(e):
        
        expences_text = expences_input.value.strip()
    
        if not expences_text.isdigit():
            print('only numbers!')
            return

        expences = int(expences_text)
        
        if expences <= 0:
            print('age must be positive!')
            return
        

        elif 0 <= expences <= 1999:
            expences_color = ft.Colors.BLUE

        elif 2000 <= expences <= 3999:
            expences_color = ft.Colors.GREEN

        elif 4000 <= expences <= 6000:
            expences_color = ft.Colors.RED
            
        else: 
            expences_color = ft.Colors.BLACK


        page.total_expences += expences

        total_expences_text.value = f'total expences: {page.total_expences}'
    

        list.controls.append(
            ft.Row(
                controls=[
                    ft.Text(value=f'name: {name_input.value} |', size=20, color=ft.colors.BLACK, bgcolor=ft.Colors.DEEP_ORANGE_50),
                    ft.Text(value=f'expences: {expences_input.value} |', size=20, color=expences_color, bgcolor=ft.Colors.DEEP_ORANGE_50),
                    ft.IconButton(icon=ft.icons.EDIT, icon_size=20, icon_color=ft.colors.BROWN),
                    ft.IconButton(icon=ft.icons.DELETE_OUTLINE, icon_size=20, icon_color=ft.colors.RED)
                ] 
            )
        )
        name_input.value = ""
        expences_input.value = ""
        

        page.update()

    name_input = ft.TextField(label="Enter name: ")
    expences_input = ft.TextField(label='Enter expences: ')
    # icons = ft.icons.ACCESS_TIME
    
    list = ft.Column(
        expand=True, scroll="alweys"
    )

    button = ft.ElevatedButton("Save it", on_click=click_button, bgcolor=ft.Colors.BROWN_800, color=ft.Colors.AMBER_800)
    row_area = ft.Row(
        controls=[name_input, expences_input, button]
    )

    

    page.add(title, row_area, total_expences_text, list)


ft.app(main)


