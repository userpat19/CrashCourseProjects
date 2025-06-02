import datetime

class Node:
    def __init__(self, visit_date, name, ailment):
        self.data = [visit_date, name, ailment]
        self.left = None
        self.right = None

class PatientBST:
    def __init__(self):
        self.root = None

    def insert(self, visit_date, name, ailment):
        def _insert(node, visit_date, name, ailment):
            if not node:
                return Node(visit_date, name, ailment)
            if visit_date < node.data[0]:
                node.left = _insert(node.left, visit_date, name, ailment)
            elif visit_date > node.data[0]:
                node.right = _insert(node.right, visit_date, name, ailment)
            return node
        self.root = _insert(self.root, visit_date, name, ailment)

    def search(self, visit_date):
        def _search(node, visit_date):
            if not node or node.data[0] == visit_date:
                return node
            if visit_date < node.data[0]:
                return _search(node.left, visit_date)
            return _search(node.right, visit_date)
        return _search(self.root, visit_date)

    def delete(self, visit_date):
        def _min_value_node(node):
            while node.left:
                node = node.left
            return node

        def _delete(node, visit_date):
            if not node:
                return None
            if visit_date < node.data[0]:
                node.left = _delete(node.left, visit_date)
            elif visit_date > node.data[0]:
                node.right = _delete(node.right, visit_date)
            else:
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                temp = _min_value_node(node.right)
                node.data = temp.data
                node.right = _delete(node.right, temp.data[0])
            return node
        self.root = _delete(self.root, visit_date)

    def inorder(self):
        def _inorder(node):
            if node:
                _inorder(node.left)
                print(f"Date: {node.data[0]}, Name: {node.data[1]}, Ailment: {node.data[2]}")
                _inorder(node.right)
        _inorder(self.root)

    def preorder(self):
        def _preorder(node):
            if node:
                print(f"Date: {node.data[0]}, Name: {node.data[1]}, Ailment: {node.data[2]}")
                _preorder(node.left)
                _preorder(node.right)
        _preorder(self.root)

    def postorder(self):
        def _postorder(node):
            if node:
                _postorder(node.left)
                _postorder(node.right)
                print(f"Date: {node.data[0]}, Name: {node.data[1]}, Ailment: {node.data[2]}")
        _postorder(self.root)


# ==== Terminal System ====
def main():
    bst = PatientBST()

    while True:
        print("\n=== Patient Record System ===")
        print("1. Insert Patient Record")
        print("2. Search Patient by Visit Date")
        print("3. Delete Patient by Visit Date")
        print("4. Display In-order Traversal (Chronological)")
        print("5. Display Pre-order Traversal")
        print("6. Display Post-order Traversal")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            date_str = input("Enter visit date (YYYY-MM-DD): ")
            try:
                visit_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
                name = input("Enter patient name: ")
                ailment = input("Enter patient ailment: ")
                bst.insert(visit_date, name, ailment)
                print("Record inserted.")
            except ValueError:
                print("Invalid date format. Try again.")
        elif choice == "2":
            date_str = input("Enter visit date to search (YYYY-MM-DD): ")
            try:
                visit_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
                result = bst.search(visit_date)
                if result:
                    print("Patient found:", result.data)
                else:
                    print("No record found for that date.")
            except ValueError:
                print("Invalid date format.")
        elif choice == "3":
            date_str = input("Enter visit date to delete (YYYY-MM-DD): ")
            try:
                visit_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
                bst.delete(visit_date)
                print("Record deleted if it existed.")
            except ValueError:
                print("Invalid date format.")
        elif choice == "4":
            print("\nIn-order Traversal:")
            bst.inorder()
        elif choice == "5":
            print("\nPre-order Traversal:")
            bst.preorder()
        elif choice == "6":
            print("\nPost-order Traversal:")
            bst.postorder()
        elif choice == "7":
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()


