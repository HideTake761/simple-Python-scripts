import PyPDF2

merger = PyPDF2.PdfMerger()

merger.append('/Users/*****/Desktop/sample01.pdf')
merger.append('/Users/*****/Desktop/sample02.pdf')

merger.write('/Users/*****/Desktop/sample_merged.pdf')
merger.close()