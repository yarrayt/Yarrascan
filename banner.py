def show_banner():
    figlet = Figlet(font='slant')
    banner = figlet.renderText('YARRASCAN')

    orange = "\033[38;5;214m"
    reset = "\033[0m"

    print(f"{orange}{banner}{reset}")
    print(f"{orange}Author : Raghav{reset}")
    print(f"{orange}Version: {VERSION}{reset}")
    print(f"{orange}Ultimate Terminal Security Toolkit{reset}")
    print(f"{orange}{'-' * 60}{reset}")
