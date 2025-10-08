class BubbleSorter:
    def __init__(self, data=None):
        self.data = data if data is not None else []

    def display(self):
        print(self.data)

    def sort(self, ascending=True):
        n = len(self.data)
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if ascending:
                    if self.data[j] > self.data[j + 1]:
                        self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
                else:
                    if self.data[j] < self.data[j + 1]:
                        self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]


# โปรแกรมหลัก
if __name__ == "__main__":
    nums = [64, 34, 25, 12, 22, 11, 90]
    sorter = BubbleSorter(nums)

    print("Before sorting:")
    sorter.display()

    sorter.sort()

    print("After sorting:")
    sorter.display()
