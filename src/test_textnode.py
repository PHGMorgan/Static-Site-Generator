import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_esq(self):
        node = TextNode('This is a normal text node', TextType.normal_text)
        node2 = TextNode('This is a normal text node', TextType.normal_text)
        node3 = TextNode('This is a bold text node', TextType.bold_text)
        node4 = TextNode('This is a bold text node', TextType.bold_text)
        node5 = TextNode('This is a italics text node', TextType.italic_text)
        node6 = TextNode('This is a italics text node', TextType.italic_text)
        node7 = TextNode('This is a code text node', TextType.code_text)
        node8 = TextNode('This is a code text node', TextType.code_text)
        node9 = TextNode('This is a link text node', TextType.normal_text, 'www.google.com')
        node10 = TextNode('This is a link text node', TextType.normal_text, 'www.google.com')
        node11 = TextNode('This is an image test node', TextType.normal_text, 'https://shorturl.at/op0T5')
        node12 = TextNode('This is an image test node', TextType.normal_text, 'https://shorturl.at/op0T5')
        node13 = TextNode('This is a normal text node', TextType.normal_text, None)
        self.assertEqual(node, node2)
        self.assertEqual(node3, node4)
        self.assertEqual(node5, node6)
        self.assertEqual(node7, node8)
        self.assertEqual(node9, node10)
        self.assertEqual(node11, node12)
        self.assertEqual(node, node13)
        self.assertNotEqual(node, node3)
        self.assertNotEqual(node3, node5)
        self.assertNotEqual(node5, node7)
        self.assertNotEqual(node7, node9)
        self.assertNotEqual(node9, node11)
        self.assertNotEqual(node, node9)
        self.assertNotEqual(node3, node9)
        self.assertNotEqual(node5, node9)
        self.assertNotEqual(node7, node9)
        self.assertNotEqual(node, node11)
        self.assertNotEqual(node3, node11)
        self.assertNotEqual(node5, node11)
        self.assertNotEqual(node7, node11)

if __name__ == '__main__':
    unittest.main()