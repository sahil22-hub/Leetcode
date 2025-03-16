class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        output = []
        l = len(searchWord)
        for i in range(l):
            temp = searchWord[:i+1]
            store = [word for word in products if word[:i+1] == temp][:3]
            output.append(store)
        print(output)
        return output

        