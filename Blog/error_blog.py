def find_error(error):
    if error.count("errorlist")==3:
        a1=error.split("<li>")[2].split(".")[0]
        a2=error.split("<li>")[4].split(".")[0]
        return f"{a1} & {a2}"
    elif error.count("errorlist")==2 and "Username already" in error:
        username_er=error.split("<li>")[2].split(".")[0]
        return username_er
    elif error.count("errorlist")==2 and "Email already" in error:
        email_er=error.split("<li>")[2].split(".")[0]
        return email_er
    else:
        print("something else")
