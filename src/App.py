
import config
import flist


def main():
    _ = flist.login(config.USER, config.PASSWORD)
    
    notes = flist.get_inbox()
    print(notes[0].show())
    
if __name__ == "__main__":
    main()
