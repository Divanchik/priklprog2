import argparse as argp
import json

parser = argp.ArgumentParser(description="Парсер для получения путей к входному и выходному файлу")
parser.add_argument("-input", type=str, default="input.txt", help="путь ко входному файлу")
parser.add_argument("-output", type=str, default="output.txt", help="путь ко выходному файлу")
args = parser.parse_args()

input_path = args.input
output_path = args.output