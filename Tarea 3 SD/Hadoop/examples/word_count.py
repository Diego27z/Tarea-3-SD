from mrjob.job import MRJob
import re
from mrjob import conf
conf.HADOOP_INPUT_FORMAT = 'org.apache.hadoop.mapred.TextInputFormat'
conf.HADOOP_OUTPUT_FORMAT = 'org.apache.hadoop.mapred.TextOutputFormat'
conf.HADOOP_HOME = '~/Descargas/hadoop-3.3.3/etc/hadoop'  # Ajusta la ruta según tu instalación


WORD_RE = re.compile(r"[\w']+")

class MRWordCount(MRJob):

    def mapper(self, _, line):
        
        for word in WORD_RE.findall(line):
            yield (word.lower(), 1)

    def combiner(self, word, counts):
        
        yield (word, sum(counts))

    def reducer(self, word, counts):
        
        yield (word, sum(counts))
        

if __name__ == '__main__':
    MRWordCount.run()