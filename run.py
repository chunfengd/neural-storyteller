import sys
import argparse
import config
import generate

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--model_cache_path', help = 'model cache path')
    parser.add_argument('--type', help = 'train or inference',default='inference')
    parser.add_argument('--input', help = 'input file')
    print("asdasd")
    args = parser.parse_args()

    if args.type == 'inference':
        config.init(args.model_cache_path)
        z = generate.load_all()
        s = generate.story(z, args.input)
        print(s)
