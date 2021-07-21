# coding: utf-8
# @Time : 7/21/21 9:08 AM


class LruList:

    def __init__(self, init_data, max_len=4):
        self.data = init_data
        self.max_len = max_len

    def _is_in_data(self, k):
        """
        仅学习时，使用这种方式直观体现时间复杂度
        :return:
        """
        for item in self.data:
            if item == k:
                return True
        return False

    def _move_data(self, k):
        new_data = [k]
        for item in self.data:
            if item == k:
                continue
            new_data.append(item)
        self.data = new_data

    def _full_insert_data(self, k):
        new_data = [k]
        for item in self.data[:-1]:
            new_data.append(item)
        self.data = new_data

    def get_value(self, k):
        # 时间复杂度 O(n)
        if self._is_in_data(k):
            self._move_data(k)
        else:
            if len(self.data) >= self.max_len:
                self._full_insert_data(k)
            else:
                self._move_data(k)


if __name__ == '__main__':
    lru_list = LruList([0, 1, 2], max_len=4)
    lru_list.get_value(-1)
    assert lru_list.data == [-1, 0, 1, 2]
    lru_list.get_value(2)
    assert lru_list.data == [2, -1, 0, 1]
    lru_list.get_value(5)
    assert lru_list.data == [5, 2, -1, 0]
