import unittest
from Stack import Stack

class StackTest(unittest.TestCase) :
    
    def test_push(self) :
        stack = Stack()
        self.assertEqual(stack.show(), [])
        stack.push('first')
        self.assertEqual(stack.show(), ['first'])
        stack.push('second')
        self.assertEqual(stack.show(), ['second', 'first'])
        stack.push('third')
        self.assertEqual(stack.show(), ['third', 'second', 'first'])
        stack.push('fourth')
        self.assertEqual(stack.show(), ['fourth', 'third', 'second', 'first'])
        stack.push('fiveth')
        self.assertEqual(stack.show(), ['fiveth', 'fourth', 'third', 'second', 'first'])

    def test_pop(self) :
        stack = Stack()
        stack.push('first')
        stack.push('second')
        stack.push('third')
        stack.push('fourth')
        stack.push('fiveth')
        self.assertEqual(stack.pop(), 'fiveth')
        self.assertEqual(stack.pop(), 'fourth')
        self.assertEqual(stack.pop(), 'third')
        self.assertEqual(stack.pop(), 'second')
        self.assertEqual(stack.pop(), 'first')
        self.assertEqual(stack.pop(), None)



    def test_peek(self) :
        stack = Stack()
        self.assertEqual(stack.peek(), None)
        stack.push('first')
        self.assertEqual(stack.peek(), 'first')
        stack.push('second')
        self.assertEqual(stack.peek(), 'second')
        stack.push('third')
        self.assertEqual(stack.peek(), 'third')
        stack.push('fourth')
        self.assertEqual(stack.peek(), 'fourth')
        stack.push('fiveth')
        self.assertEqual(stack.peek(), 'fiveth')
        self.assertEqual(stack.show(), ['fiveth', 'fourth', 'third', 'second', 'first'])

    def test_util(self) :
        pass

if __name__ == '__main__':
    unittest.main()
