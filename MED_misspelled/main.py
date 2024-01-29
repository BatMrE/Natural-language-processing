import multiprocessing as mp
import time
from src.data import download_file, dat_to_df
from src.operations import calculate_top_words, success_top_k, average_success_top_k

class Main:
    def __init__(self):
        pass

    def greet(self, name):
        pass

    def run(self):
        pass

if __name__ == "__main__":
    main_instance = Main()
    main_instance.run()

    url = 'https://www.dcs.bbk.ac.uk/~roger/missp.dat'
    save_path = 'sample.dat'
    output_file_path = 'dat_to_txt.txt'
    dat_file_path = 'PERIN2DAT.643'
    download_file(url, save_path)
    df = dat_to_df(dat_file_path, output_file_path)

    start_time = time.time()
    pool = mp.Pool()
    top_k_result = pool.map(calculate_top_words, df.values.tolist()[:10])
    # top_k_result = []
    # top_k_result.append(pool.map(calculate_top_words, df.values.tolist()))
    pool.close()
    pool.join()
    print("Execution time:", time.time() - start_time)

    success = success_top_k(top_k_result[0])
    avg_success = average_success_top_k(success)
    print(avg_success)