# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class WrappableInt:
    def __init__(self, x):
        self.value = x

    def getValue(self):
        return self.value

    def increment(self):
        self.value += 1


class Codec:

    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """
        serializedList = []
        self._serializeHelper(root, serializedList)
        return "".join(serializedList)

    def _serializeHelper(self, root, serializedList):
        if not root:
            return

        # Actual value
        serializedList.append(chr(root.val + 48))

        # Number of children
        serializedList.append(chr(len(root.children) + 48))

        for child in root.children:
            self._serializeHelper(child, serializedList)

    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """

        if not data:
            return None

        return self._deserializeHelper(data, WrappableInt(0))

    def _deserializeHelper(self, data, index):

        if index.getValue() == len(data):
            return None

        # The invariant here is that the "index" always
        # points to a node and the value next to it
        # represents the number of children it has.
        node = Node(ord(data[index.getValue()]) - 48, [])
        index.increment()
        numChildren = ord(data[index.getValue()]) - 48
        for _ in range(numChildren):
            index.increment()
            node.children.append(self._deserializeHelper(data, index))
        return node
