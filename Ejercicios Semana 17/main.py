from finance_logic import FinanceManager
from interface_app import main_layout
import FreeSimpleGUI as sg

def main():
    try:
        # Initialize logic loading data
        manager = FinanceManager()
        
        # Starts Graphical User Interface
        main_layout(manager)
        
    except Exception as e:
        sg.popup_error(f"Fatal error during execution: {e}")

if __name__ == "__main__":
    main()