def adult(something):
    try:
        print("Age is " + something)
    except:
        print("Fail to concat")
    finally:
        print("Evething is fine.")


adult(20)
