from helper_functions import copy_static
from generator import generate_page
def main():
    copy_static("/home/ec2-user/sitegen/static", "/home/ec2-user/sitegen/public")
    generate_page("content/index.md", "template.html", "public/index.html")

main()
