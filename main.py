from session import ODCSession

def main():
    session = ODCSession(simulate_mri_trigger=True)
    session.run()

if __name__ == '__main__':
    main()
