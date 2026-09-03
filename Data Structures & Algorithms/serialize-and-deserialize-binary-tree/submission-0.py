class Codec:

    def serialize(self, root):
        result = []

        def dfs(node):
            if node is None:
                result.append("N")
                return

            result.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return ",".join(result)

    def deserialize(self, data):
        values = data.split(",")
        index = 0

        def dfs():
            nonlocal index

            if values[index] == "N":
                index += 1
                return None

            node = TreeNode(int(values[index]))
            index += 1

            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()