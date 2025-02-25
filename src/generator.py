from html_generator import markdown_to_html_node
from htmlnode import HTMLNode, ParentNode, LeafNode
from textnode import TextNode, extract_title
import os

def generate_page(from_path, template_path, dest_path):
    
    
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
