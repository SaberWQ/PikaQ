import Project

def main():
    try:
        Project.execute()  
        Project.project.run(port = 8000 ,debug = True)
    except Exception as error:
        print(error)

if __name__ == '__main__':
    main()

# echo "# PikaQ" >> README.md
# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/SaberWQ/PikaQ.git
# git push -u origin main