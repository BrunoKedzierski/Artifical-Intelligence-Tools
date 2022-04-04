from file_processor import FileProcessor


processor = FileProcessor(['de','en','pl'],'.',2, 600)
processor.process()
freqs = processor.char_frequencies
