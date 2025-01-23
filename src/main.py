from textnode import *

def main():
    test = TextNode('Test', TextType.bold_text, 'https://i0.wp.com/southcountynews.org/wp-content/uploads/2023/06/Picture-Walks-blue-gray-gnatcher-as-an-Angry-Bird.jpg?ssl=1')
    print(test.__repr__())
    return

if __name__ == '__main__':
    main()