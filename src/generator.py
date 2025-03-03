from html_generator import markdown_to_html_node
from htmlnode import HTMLNode, ParentNode, LeafNode
from textnode import TextNode, extract_title
import os, shutil

def generate_page(from_path, template_path, dest_path, basepath):
    
    
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    

    
    # Read markdown file
    
    try:
        
        with open(from_path, 'r') as f:
            
            markdown_content = f.read()
            
    except FileNotFoundError:
        
        raise Exception(f"Markdown file not found at {from_path}")
    

    
    # Read template file
    
    try:
        
        with open(template_path, 'r') as f:
            
            template_content = f.read()
            
    except FileNotFoundError:
        
        raise Exception(f"Template file not found at {template_path}")
    

    
    # Convert markdown to HTML
    title = extract_title(markdown_content)
    
    html_node = markdown_to_html_node(markdown_content)
    
    html_content = html_node.to_html()
    

    final_html = template_content.replace("{{ Title }}", title)

    final_html = final_html.replace("{{ Content }}", html_content)
   
    final_html = final_html.replace('href="/', f'href="{basepath}').replace('src="/', f'src="{basepath}')
    
    # Create destination directory if it doesn't exist
    
    dest_dir = os.path.dirname(dest_path)
    
    if dest_dir:
        
        try:
            
            os.makedirs(dest_dir, exist_ok=True)
            
        except Exception as e:
            
            raise Exception(f"Failed to create directory {dest_dir}: {str(e)}")

    try:
        with open(dest_path, "w") as outfile:
            outfile.write(final_html)
    except Exception as e:
        raise Exception(f"Failed to write HTML file to {dest_path}: {str(e)}")


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    os.makedirs(dest_dir_path, exist_ok=True)
    for item in os.listdir(dir_path_content):
        item_path = os.path.join(dir_path_content, item)
        if os.path.isfile(item_path):
            if item.endswith(".md"):
                print(f"Creating .html file from: {item_path}")
                dest_file = item.replace(".md", ".html")
                dest_path = os.path.join(dest_dir_path, dest_file)
                generate_page(item_path, template_path, dest_path, basepath)

        else:
            dir_path = os.path.join(dir_path_content, item)
            copy_path = os.path.join(dest_dir_path, item)
            print(f"Creating directory: {copy_path}")
            generate_pages_recursive(dir_path, template_path, copy_path, basepath)
