# f = open("README.md", "w")
# f.write("This is an emotional analyzer project, created by Rochit")
# f.close()

with open("README.md","a") as fs:
    fs.write("\nFor personal use only")

with open("README.md","r") as f:
    print(f.read())