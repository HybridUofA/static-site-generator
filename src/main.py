from helper_functions import copy_static
from generator import generate_pages_recursive
import sys

def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    copy_static("/home/ec2-user/sitegen/static", "/home/ec2-user/sitegen/public")
    generate_pages_recursive("content", "template.html", "docs", basepath)

main()
