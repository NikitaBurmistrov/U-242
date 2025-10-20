from terminal import Terminal

if __name__ == "__main__":
    terminal1 = Terminal()
    print(terminal1)
    while True:
        terminal1.show_menu()
        menu_item = input()
        terminal1.process_command(menu_item)