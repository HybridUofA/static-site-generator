from helper_functions import copy_static
from generator import generate_pages_recursive
def main():
    copy_static("/home/ec2-user/sitegen/static", "/home/ec2-user/sitegen/public")
    generate_pages_recursive("content", "template.html", "public")

main()
