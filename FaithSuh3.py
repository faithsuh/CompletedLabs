import sys
import formulas


def main():
    numbers = []
    input_list = sys.argv[2:]
    if len(sys.argv) <= 1:
        sys.exit('Need to provide operator')
    elif len(sys.argv) <= 3:
        sys.exit('Need to provide at least two values')
    else:
        for i in input_list:
            numbers.append(float(i))
        if 'add' in sys.argv:
            print(f'Answer = {formulas.add(numbers):.2f}')
        elif 'subtract' in sys.argv:
            print(f'Answer = {formulas.subtract(numbers):.2f}')
        elif 'multiply' in sys.argv:
            print(f'Answer = {formulas.multiply(numbers):.2f}')
        elif 'divide' in sys.argv:
            print(f'Answer = {formulas.divide(numbers):.2f}')
        else:
            sys.exit('Valid operator names (add, subtract, multiply, divide)')


if __name__ == '__main__':
    main()
