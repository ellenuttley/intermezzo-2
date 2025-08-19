class DiaryEntry:
    def __init__(self, title, contents): 
        self.title = title
        self.contents = contents
        self.chunk_count = 0
        self.chunks = []

    def count_words(self):
        return len(self.contents.split())

    def reading_time(self, wpm):
        word_count = self.count_words()
        word_time = 60 / wpm

        total_seconds = word_count * word_time
        return int(total_seconds // 60)

    def reading_chunk(self, wpm, minutes):
        total_length = wpm * minutes
        words = self.contents.split(' ')
        self.make_chunks(words, total_length)
        try:
            print(self.chunks[self.chunk_count])
            return ' '.join(self.chunks[self.chunk_count])
        finally:
            self.chunk_count += 1
    
    def make_chunks(self, words, total_length):
        self.chunks = [words[i:i + total_length] for i in range(0, len(self.contents), total_length)]
