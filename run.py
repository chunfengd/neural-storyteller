import sys,time
import argparse
import config
import generate

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--model_cache_path', help = 'model cache path')
    parser.add_argument('--type', help = 'train or inference',default='inference')
    parser.add_argument('--input', help = 'input file')
    parser.add_argument('--condition_count', type=int,default=100)
    parser.add_argument('--beamwidth', type=int,default=50)
    args = parser.parse_args()

    print args

    if args.type == 'inference':
        config.init(args.model_cache_path)
        z = generate.load_all()
        s = generate.story(z, args.input,args.condition_count,args.beamwidth)
        #s = generate.story(z, args.input)
        output_file = '/data/output/{}.txt'.format(str(int(time.time())));
        with open(output_file, "w") as f:
            f.write('{}'.format(s))
        print output_file
