import sys,time
import argparse
import config
import generate

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--model_cache_path', help = 'model cache path')
    parser.add_argument('--type', help = 'train or inference')
    parser.add_argument('--input', help = 'input file')
    args = parser.parse_args()

    if args.type == 'inference':
        config.init(args.model_cache_path)
        z = generate.load_all()
        s = generate.store(z, args.input)
        output_file = '/data/output/{}.txt'.format(str(int(time.time())));
        with open(output_file, "w") as f:
            f.write('result:\n{}'.format(s))
        print output_file
