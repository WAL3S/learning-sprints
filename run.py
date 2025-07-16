import sys

def usage():
    print("Usage: python run.py [converter|quiz]")
    
def main():
    if len(sys.argv) != 2:
        usage()
        return
    choice = sys.argv[1].lower()
    if choice=="converter":
        import myapp.converter as mod; mod.main()
    elif choice=="quiz":
        import myapp.quizzer as mod; mod.main()
    else:
        usage()

if __name__ == "__main__":
    main()
