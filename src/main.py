import flet as ft

def main(page: ft.Page):
    page.title = "Hi Guys"

    friends = ["Tima", "Beka", "Adi"]

    result_text = ft.Text()

    def find_name(e):
        input_value = name_input.value.strip().title()
        if input_value in friends:
            result_text.value = f"✅ Drug: {input_value}"
        else:
            result_text.value = "❌ Ne drug."
        page.update()

    name_input = ft.TextField(label="Enter name", on_change=find_name)
    
    page.add(name_input, result_text)

ft.app(main)
