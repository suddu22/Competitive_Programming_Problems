"""
External Sort
"""
import heapq
class ExternalSort:
    def __init__(self, buffer_size, file_name):
        self.buffer_size = buffer_size
        self.file_name = file_name
        self.split_count = 0

    def file_spliter_sort(self, sort_key):

        large_file = open(self.file_name, 'r')
        done = False
        while not done:
            lines = large_file.read(self.buffer_size)
            if not lines:
                break

            lines = sorted(lines, key=sort_key)

            sorted_file = open(str(self.split_count), 'w')
            sorted_file.write(lines)
            sorted_file.close()
            self.split_count += 1
        large_file.close()

    def merge_sorted_files(self):

        file_buffer_size = self.buffer_size / (self.split_count + 1)
        files_table = {}
        heap_list = []

        for f in range(self.split_count):
            current_file = open(str(f), 'r', file_buffer_size)
            files_table[f] = current_file

        for f in range(self.split_count):
            lines = files_table[f]
            for line in lines:
                l = line.split(',')
                heapq.heappush(heap_list, (l[1], l[0], l[2]))

        out_file = open("final_file", 'w+')
        while len(heap_list) > 0:
            line = heapq.heappush(heap_list)
            out_file.write(line)
        out_file.close()



