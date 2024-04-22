import curses as curses
def print_menu(stdscr, selected_row_idx, options, additional_text=None):
    stdscr.clear()
    h, w = stdscr.getmaxyx()

    # Print additional text
    if additional_text:
        stdscr.addstr(h//2 - len(options)//2 - 2, w//2 - len(additional_text)//2, additional_text)

    for idx, option in enumerate(options):
        x = w//2 - len(option)//2
        y = h//2 - len(options)//2 + idx
        if idx == selected_row_idx:
            stdscr.attron(curses.A_REVERSE)
            stdscr.addstr(y, x, option)
            stdscr.attroff(curses.A_REVERSE)
        else:
            stdscr.addstr(y, x, option)

    stdscr.refresh()

def player_select_screen(stdscr):
    curses.curs_set(0)
    stdscr.keypad(True)

    # options = next_posible_pisitions(game_map,player.get_entity_position())
    options = ["Right","Left","Stright"]
    selected_row_idx = 0

    print_menu(stdscr, selected_row_idx, options, additional_text="Additional text here")

    while True:
        key = stdscr.getch()

        if key == curses.KEY_UP or key == ord('w'):
            selected_row_idx = max(0, selected_row_idx - 1)
        elif key == curses.KEY_DOWN or key == ord('s'):
            selected_row_idx = min(len(options) - 1, selected_row_idx + 1)
        elif key == curses.KEY_ENTER or key in [10, 13]:
            return options[selected_row_idx]

        print_menu(stdscr, selected_row_idx, options, additional_text="Additional text here")
print(curses.wrapper(player_select_screen))
