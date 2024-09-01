from functools import cache
import os
from utils import File, Log

log = Log('DDC')

class DDC:
    DATA_PATH = os.path.join('data', 'ddc.txt')
    @staticmethod
    @cache
    def load_idx():
        lines = File(DDC.DATA_PATH).read_lines()
        idx = {}
        for line in lines:
            if line.startswith('Class'):
                continue
            code, _, description = line.partition(' ')  
            idx[code] = description.strip()

        n = len(idx)
        log.info(f'Loaded {n} DDC codes from {DDC.DATA_PATH}')
        return idx
    
    @staticmethod
    @cache
    def get(code):
        idx = DDC.load_idx()
        return idx.get(str(code))