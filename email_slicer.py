def email_slicer():
    print(" Welcome to the Email Slicer ")
    print("")

    email_to_slice = input("Input email you wish to slice: ")

    (username, domain) = email_to_slice.split("@")
    (domain, extension) = domain.split(".")

    print(f"UserName: {username}")
    print(f"Domain: {domain}")
    print(f"Extension: {extension}")


email_slicer()
